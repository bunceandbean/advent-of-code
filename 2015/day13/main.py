from itertools import permutations
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]

def happiness(perm, happy_obj):
    total = 0
    for i in range(len(perm)):
        one = i
        two = (i + 1) % len(perm)
        total += happy_obj[perm[one]][perm[two]]
        total += happy_obj[perm[two]][perm[one]]
    return total

happy = {}
me_happy = {'Me':{}}
names = []
me_names = ["Me"]
for line in content:
    name = line[:line.index("would")-1]
    flop = 1
    next_to = line[line.index("to")+3:len(line)-1]
    num = int(line[line.index("would")+11:line.index("hap")-1])
    if name not in happy.keys():
        happy[name] = {}
        me_happy[name] = {'Me':0}
        me_happy['Me'][name] = 0
        names.append(name)
        me_names.append(name)
    if 'lose' in line:
        flop = -1
    happy[name][next_to] = flop*num
    me_happy[name][next_to] = flop*num

tables = list(permutations(names))
me_tables = list(permutations(me_names))

def get_max_happy(table,happy_obj):
    max_good = 0
    for perm in table:
        num = happiness(perm,happy_obj)
        if num > max_good:
            max_good = num
    return max_good


answer_one = str(get_max_happy(tables,happy))
answer_two = str(get_max_happy(me_tables,me_happy))
print("p1: " + answer_one)
print("p2: " + answer_two)
