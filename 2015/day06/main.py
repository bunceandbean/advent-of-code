with open("input.txt") as f:
    content = f.readlines()
    content = [x.strip("\n") for x in content]

def light_grid(nordic):
    grid = {}
    for rule in content:
        yStart = int(rule[rule.index(",")+1:rule.index("th")-1])
        temp = rule[rule.index(",")+1:]
        xEnd = int(temp[temp.index("gh") + 3: temp.index(",")])
        yEnd = int(temp[temp.index(",") + 1:])
        if "turn on" in rule:
            xStart = int(rule[rule.index("on") + 3:rule.index(",")])
            set = 1
        elif "turn off" in rule:
            xStart = int(rule[rule.index("off") + 4:rule.index(",")])
            set = 0
        else:
            xStart = int(rule[rule.index("gle") + 4:rule.index(",")])
            set = -1
        for i in range(xStart,xEnd +1):
            for j in range(yStart,yEnd + 1):
                if (i,j) not in grid:
                    grid[(i,j)] = 0
                if set == -1:
                    if not nordic:
                        grid[(i,j)] = abs(grid[(i,j)] + set)
                    else:
                        grid[(i,j)] = grid[(i,j)] + 2
                elif set == 1 and nordic:
                    grid[(i,j)] += 1
                elif set == 0 and nordic:
                    grid[(i,j)] -= 1
                    if grid[(i,j)] < 0:
                        grid[(i,j)] = 0
                else:
                    grid[(i,j)] = set
    if not nordic:
        return str(sum(value == 1 for value in grid.values()))
    else:
        return sum(value for value in grid.values())

answer_one = str(light_grid(False))
answer_two = str(light_grid(True))

print("p1: " + answer_one)
print("p2: " + answer_two)
