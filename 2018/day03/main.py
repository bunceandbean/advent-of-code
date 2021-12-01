with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

unique = set()
overlaps = set()
fabric = []
id = ""
l = 0
for line in content:
    fabric.append([])
    x = int(line[line.index("@") + 2:line.index(",")])
    y = int(line[line.index(",") + 1:line.index(":")])
    x_r = int(line[line.index(":") + 2:line.index("x")])
    y_r = int(line[line.index("x") + 1:])
    for i in range(y_r):
        for j in range(x_r):
            fabric[l].append(((x+j,y+i)))
            length = len(unique)
            unique.add((x+j,y+i))
            if length == len(unique):
                overlaps.add((x+j,y+i))
    l += 1

def find_non():
    for sq in fabric:
        laps = False
        for point in sq:
            if point in overlaps:
                laps = True
        if not laps:
            return str(fabric.index(sq) + 1)
    return ""


answer_one = str(len(overlaps))
answer_two = find_non()
print("p1: " + answer_one)
print("p2: " + answer_two)
