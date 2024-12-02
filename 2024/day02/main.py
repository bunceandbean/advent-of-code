with open("input.txt") as f:
    content = [list(map(int, x.split(" "))) for x in f.read().split("\n")[:~0]]

def test_row(row):
    dir = row[1] - row[0]
    for i in range(1,len(row)):
        if not (((row[i] - row[i-1]) * dir > 0) and abs(row[i] - row[i-1]) in [1,2,3]):
           return False
    return True

total = 0
tolerate = 0
for row in content:
    total += test_row(row)
    tolerate += True in [test_row(row[:i] + row[i+1:]) for i in range(len(row))]
    
print("p1:", total)
print("p2:", tolerate)