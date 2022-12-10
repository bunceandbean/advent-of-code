with open("input.txt") as f:
    content = [x.split(" ") for  x in f.read().split("\n")[:~0]]

order = []
for line in content:
    order.append(0)
    if line[0] == "addx":
        order.append(int(line[1]))

def run(order,render):
    total = 0
    x = 1
    vals = [20,60,100,140,180,220]
    for i in range(len(order)):
        if not render and i + 1 in vals:
            total += x * vals.pop(0)
        if render:
            print('*' if abs(i % 40 - x) <= 1 else ' ', end='' if (i+1) % 40 else '\n')
        x += order[i]
    return total


answer_one, answer_two = run(order, False), run(order, True)
print("p1:", answer_one)
