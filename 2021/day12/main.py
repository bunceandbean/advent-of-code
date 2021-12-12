from collections import defaultdict
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

paths = defaultdict(list)
for line in content:
    one,two = line.split('-')
    paths[one].append(two)
    paths[two].append(one)

def pathfinder(pos,past,mult,cave):
    poss = 0
    if pos == "end":
        return 1
    if pos == "start" and len(past) != 0:
        return 0
    if pos.islower() and pos in past and not mult:
        return 0
    elif pos.islower() and pos in past and mult:
        if cave == "":
            cave = pos
        else:
            return 0
    for route in paths[pos]:
        poss += pathfinder(route,past | {pos},mult,cave)
    return poss


answer_one = pathfinder("start",set(),False,"")
answer_two = pathfinder("start",set(),True,"")
print("p1:",answer_one)
print("p2:",answer_two)
