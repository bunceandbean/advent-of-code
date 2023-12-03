with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

ids = set(int(line[line.index("#")+1:line.index("b")-1]) for line in content if "#" in line)

def dates(c):
    return int(c[c.index("-")+1:c.index("-")+3]+c[c.index("-")+4:c.index(" ")]) 

content.sort(key=dates)
for line in content:
    print(line)

#answer_one =
#answer_two =
#print("p1: " + answer_one)
#print("p2: " + answer_two)
