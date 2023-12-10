from math import lcm
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    inst = content[0].replace("L", "0").replace("R", "1")
    paths = {x[:x.index(" ")]: (x[x.index("(")+1:x.index(",")], x[x.index(",") + 2:x.index(")")]) for x in content[2:]}

def day08_1():
    i = 0
    steps = 0
    cur = "AAA"
    while cur != 'ZZZ':
        cur = paths[cur][int(inst[i])]
        i = (i + 1) % len(inst)
        steps += 1
    return steps

def check_z(cur):
    return cur[2] == 'Z'

def day08_2():
    i = 0
    steps = 0
    curs = [x for x in paths.keys() if x[2] == 'A']
    cur_cycle = [0 for _ in range(len(curs))]
    while 0 in cur_cycle:
        steps += 1
        for j in range(len(curs)):
            curs[j] = paths[curs[j]][int(inst[i])]
            if check_z(curs[j]) and cur_cycle[j] == 0:
                cur_cycle[j] = steps
        i = (i + 1) % len(inst)
    return lcm(*cur_cycle)

print("p1:", day08_1())
print("p2:", day08_2())

