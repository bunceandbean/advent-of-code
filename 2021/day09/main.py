import math
with open("input.txt") as f:
    content = [[int(m) for m in x] for x in f.read().split("\n")][:~0]

def find_neighbors(line,chr):
    neighbors = []
    if chr != 0:
        neighbors.append([content[line][chr-1],(line,chr-1)])
    if chr != len(content[line])-1:
        neighbors.append([content[line][chr+1],(line,chr+1)])
    if line != 0:
        neighbors.append([content[line-1][chr],(line-1,chr)])
    if line != len(content)-1:
        neighbors.append([content[line+1][chr],(line+1,chr)])
    return neighbors


lows = []

def basin():
    num = 0
    for line in range(len(content)):
        for chr in range(len(content[line])):
            neighbors = find_neighbors(line,chr)
            if content[line][chr] < min([x[0] for x in neighbors]):
                    num += content[line][chr] + 1
                    lows.append((line,chr))
    return num

def flood(line,chr):
    fill = {(line,chr)}
    for tup in [m[1] for m in find_neighbors(line,chr)]:
        if content[tup[0]][tup[1]] != 9 and content[tup[0]][tup[1]] > content[line][chr]:
            fill.update(flood(tup[0],tup[1]))
    return fill

answer_one = basin()
answer_two = math.prod(sorted([len(flood(tup[0],tup[1])) for tup in lows])[~2:])
print("p1:",answer_one)
print("p2:",answer_two)
