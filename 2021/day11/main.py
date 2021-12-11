with open("input.txt") as f:
    content = [[*map(int,list(x))] for x in f.read().split("\n")[:~0]]
    next_to = [(0,-1),(0,1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    points = set()

def find_neighbors(y,x):
    neighbors = [(y+pair[0],x+pair[1]) for pair in next_to \
    if (y+pair[0],x+pair[1]) in points]
    return neighbors

for y in range(len(content)):
    for x in range(len(content[y])):
        points.add((y,x))

flashes = 0
all_flash = 0
for i in range(500):
    flash = set()
    content = [[num + 1 for num in x] for x in content]
    while True:
        to_add = []
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
    if i < 100:
        flashes += len(flash)
    if all_flash == 0 and len(flash) == len(content[0]*len(content)):
        all_flash = i + 1
        break

answer_one = flashes
answer_two = all_flash
print("p1:",answer_one)
print("p2:",answer_two)
