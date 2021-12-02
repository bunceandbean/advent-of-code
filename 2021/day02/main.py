with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

depth = 0
hor = 0
depth2 = 0
for line in content:
    if "up" in line:
        depth -= int(line[line.index(" ")+1:])
    elif "down" in line:
        depth += int(line[line.index(" ")+1:])
    elif "forward" in line:
        hor += int(line[line.index(" ")+1:])
        depth2 += depth * int(line[line.index(" ")+1:])
        
answer_one = str(depth * hor)
answer_two = str(depth2 * hor)
print("p1: " + answer_one)
print("p2: " + answer_two)
