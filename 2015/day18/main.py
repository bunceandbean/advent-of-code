from copy import deepcopy
with open("input.txt") as f:
    content = f.read().split("\n")

def switch(y,x,grid,corners):
    amt = 0
    if x != 99 and grid[y][x+1] == "#":
        amt += 1
    if x != 0 and grid[y][x-1] == "#":
        amt += 1
    if y != 99 and grid[y+1][x] == "#":
        amt += 1
    if y != 0 and grid[y-1][x] == "#":
        amt += 1
    if (y!=0 and x!=0) and (grid[y-1][x-1] == "#"):
        amt += 1
    if (y!=0 and x!=99) and (grid[y-1][x+1] == "#"):
        amt += 1
    if (y!=99 and x!=0) and (grid[y+1][x-1] == "#"):
        amt += 1
    if (y!=99 and x!=99) and (grid[y+1][x+1] == "#"):
        amt += 1
    if corners and ((x==0 and y==99) or (x==0 and y==0) or (x==99 and y==0) or (x==99 and y==99)):
        return "#"
    elif amt == 3 and grid[y][x] == ".":
        return "#"
    elif (amt == 2 or amt == 3) and grid[y][x] == "#":
        return "#"
    else:
        return "."

def conway(times,corners):
    old_grid = [list(x) for x in content[:len(content)-1]]
    if corners:
        old_grid[0][0] = "#"
        old_grid[0][99] = "#"
        old_grid[99][0] = "#"
        old_grid[99][99] = "#"
    on = 0
    for i in range(times):
        new_grid = []
        for y in range(100):
            new_grid.append([])
            for x in range(100):
                char = switch(y,x,old_grid,corners)
                if char == "#" and i == times-1:
                    on += 1
                new_grid[y].append(char)
        old_grid = deepcopy(new_grid)
    return on

answer_one = str(conway(100,False))
answer_two = str(conway(100,True))
print("p1: " + answer_one)
print("p2: " + answer_two)
