answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

ranges = []
error_rate = 0

def valid(num):
    rate = 0
    amt_range = 0
    for range in ranges:
        if int(num) < range[1] and int(num) > range[0]:
            amt_range += 1
    if amt_range == 0:
        return int(num)
    return 0

for line in content:
    if "-" in line:
        r1 = line[line.index(":")+2:line.index(" or")]
        r1 = [int(r1[:r1.index("-")]),int(r1[r1.index("-")+1:])]
        r2 = line[line.index(" or")+4:]
        r2 = [int(r2[:r2.index("-")]),int(r2[r2.index("-")+1:])]
        ranges.append(r1)
        ranges.append(r2)

content = content[content.index("nearby tickets:")+1:]

for line in content:
    line = line.split(",")
    for num in line:
        error_rate += valid(num)

answer = error_rate
print(answer)
