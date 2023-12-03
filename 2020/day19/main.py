with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

rules = {}

for line in content[:content.index("")]:
    rules[int(line[:line.index(":")])] = [int(x) if x.isnumeric() else x for x in line[line.index(":") + 2:].split(" ")]
    if '"a"' in rules[int(line[:line.index(":")])]:
        rules[int(line[:line.index(":")])] = "a"
    elif '"b"' in rules[int(line[:line.index(":")])]:
        rules[int(line[:line.index(":")])] = "b"

content = content[content.index("") + 1:]

#answer_one =
#answer_two =
#print("p1:", answer_one)
#print("p2:", answer_two)
