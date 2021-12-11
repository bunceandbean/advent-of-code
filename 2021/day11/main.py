with open("input.txt") as f:
    content = [list(map(int,list(x))) for x in f.read().split("\n")[:~0]]
    next_to = [(0,-1),(0,1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    points = set()

for y in range(len(content)):
    for x in range(len(content[y])):
        points.add((y,x))

def find_neighbors(line,chr):
    neighbors = []
    for tup in next_to:
        if (line+tup[0],chr+tup[1]) in points:
            neighbors.append((line+tup[0],chr+tup[1]))
    return neighbors


flashes = 0
all_flash = 0
for i in range(1000):
    flash = set()
    to_add = []
    for y in range(len(content)):
        for x in range(len(content[y])):
            content[y][x] += 1
    while True:
        for y in range(len(content)):
            for x in range(len(content[y])):
                if content[y][x] > 9:
                    flash.add((y,x))
                    content[y][x] = 0
                    for point in find_neighbors(y,x):
                        to_add.append(point)
        for point in to_add:
            if point not in flash:
                content[point[0]][point[1]] += 1
        if len(to_add) == 0:
            break
        to_add = []
    if i < 100:
        flashes += len(flash)
    if all_flash == 0 and len(flash) == len(content[0]*len(content)):
        all_flash = i + 1


answer_one = flashes
answer_two = all_flash
print("p1:",answer_one)
print("p2:",answer_two)
