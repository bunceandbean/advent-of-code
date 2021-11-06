from math import ceil
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:~0]

boss = [int(content[x][content[x].index(":")+2:]) for x in range(len(content))]
weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
armor = [[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5],[0,0,0]]
rings = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3],[0,0,0]]

def battle(hp,dam,arm):
    if dam <= 0:
        return False
    me = boss[1] - arm
    bo = dam - boss[2]
    if me <= 0:
        me = 1
    if bo <= 0:
        bo = 1
    if ceil(hp / me) >= ceil(boss[0] / bo):
        return True
    return False

min_cost = 1000
max_cost = 0
for i in range(len(weapons)):
    for j in range(len(armor)):
        for k in range(len(rings)):
            for m in range(len(rings)):
                if m == k:
                    continue
                cost = weapons[i][0] + armor[j][0] + rings[k][0] + rings[m][0]
                if battle(100,weapons[i][1]+rings[k][1]+rings[m][1],armor[j][2]+rings[k][2]+rings[m][2]):
                    if cost < min_cost:
                        min_cost = cost
                else:
                    if cost > max_cost:
                        max_cost = cost


answer_one = str(min_cost)
answer_two = str(max_cost)
print("p1: " + answer_one)
print("p2: " + answer_two)
