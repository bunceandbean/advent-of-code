import math
with open("input.txt") as f:
    content = [[int(m) for m in x] for x in f.read().split("\n")][:~0]
    next_to = [(0,-1),(0,1),(-1,0),(1,0)]

points = set()
for i in range(len(content)):
    for j in range(len(content[0])):
        points.add((i,j))

def find_neighbors(line,chr):
    neighbors = []
    for tup in next_to:
        if (line+tup[0],chr+tup[1]) in points:
            neighbors.append([content[line+tup[0]][chr+tup[1]],(line+tup[0],chr+tup[1])])
    return neighbors


basin_lens = []
def basin():
    num = 0
    for line in range(len(content)):
        for chr in range(len(content[line])):
            neighbors = find_neighbors(line,chr)
            if content[line][chr] < min([x[0] for x in neighbors]):
                    num += content[line][chr] + 1
                    basin_lens.append(len(flood(line,chr)))
    return num

def flood(line,chr):
    fill = {(line,chr)}
    for tup in [m[1] for m in find_neighbors(line,chr)]:
        if content[tup[0]][tup[1]] != 9 and content[tup[0]][tup[1]] > content[line][chr]:
            fill.update(flood(tup[0],tup[1]))
    return fill

answer_one = basin()
answer_two = math.prod(sorted(basin_lens)[~2:])
print("p1:",answer_one)
print("p2:",answer_two)
