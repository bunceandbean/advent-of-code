from copy import deepcopy
with open("input.txt") as f:
    content = [[True if m=="#" else False for m in list(x)] \
    for x in f.read().split("\n")[:~0]]
    next_to = set()
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                if (i,j,k) != (0,0,0):
                    next_to.add((i,j,k))
    next_hyper = set()
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                for w in range(-1,2,1):
                    if (i,j,k,w) != (0,0,0,0):
                        next_hyper.add((i,j,k,w))

def find_neighbors(x,y,z,points):
    neighbors = [(z+pair[2],y+pair[1],x+pair[0]) for pair in next_to \
    if (z+pair[2],y+pair[1],x+pair[0]) in points]
    return neighbors

def find_hypers(x,y,z,w):
    neighbors = [(w+pair[3],z+pair[2],y+pair[1],x+pair[0]) for pair in next_hyper]
    return neighbors

def cycle(start,times):
    points = set()
    flop = set()
    start = [start.copy()]
    on = 0
    for i in range(times):
        for layer in range(len(start)):
            for row in start[layer]:
                row.insert(0,False)
                row.append(False)
            start[layer].insert(0,[False for x in start[0][0]])
            start[layer].append([False for x in start[0][0]])
        start.insert(0,[[False for m in range(len(start[0][0]))] for x in range(len(start[0]))])
        start.append([[False for m in range(len(start[0][0]))] for x in range(len(start[0]))])
        for z in range(len(start)):
            for y in range(len(start[z])):
                for x in range(len(start[z][y])):
                    points.add((z,y,x))
        for z in range(len(start)):
            for y in range(len(start[z])):
                for x in range(len(start[z][y])):
                    neighbors = sum([start[x[0]][x[1]][x[2]] for x in find_neighbors(x,y,z,points)])
                    if start[z][y][x] and not (neighbors == 2 or neighbors == 3):
                        flop.add((z,y,x))
                    elif not start[z][y][x] and neighbors == 3:
                        flop.add((z,y,x))
        for point in flop:
            start[point[0]][point[1]][point[2]] = not start[point[0]][point[1]][point[2]]
        flop = set()
    for z in range(len(start)):
        for y in range(len(start[z])):
            for x in range(len(start[z][y])):
                if start[z][y][x]:
                    on += 1
    return on

def hyper_cycle(start,times):
    cubes = {}
    for y in range(len(start)):
        for x in range(len(start[0])):
            cubes[(0,0,y,x)] = start[y][x]
    for i in range(times):
        to_add = set()
        flop = set()
        for cube in cubes:
            for point in find_hypers(cube[3],cube[2],cube[1],cube[0]):
                if point not in cubes:
                    to_add.add(point)
        for point in to_add:
            cubes[point] = False
        for cube in cubes:
            sums = 0
            for point in find_hypers(cube[3],cube[2],cube[1],cube[0]):
                try:
                    sums += cubes[point]
                except:
                    pass
            if cubes[cube] and not (sums == 2 or sums == 3):
                flop.add(cube)
            elif not cubes[cube] and sums == 3:
                flop.add(cube)
        for point in flop:
            cubes[point] = not cubes[point]
    return sum(cubes.values())


answer_one = cycle(deepcopy(content),6)
answer_two = hyper_cycle(deepcopy(content),6)
print("p1:",answer_one)
print("p2:",answer_two)
