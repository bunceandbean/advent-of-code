#Open file and compress contents into an array
from copy import deepcopy
with open("input.txt") as f:
    content = f.read().split("\n")
    content = [list(x) for x in content]
    content = content[:len(content)-1]

# y,x
def nodes(grid, times):
    delta = [-1,0]
    infects = 0
    pos = [len(grid) // 2] * 2
    for i in range(times):
        if grid[pos[0]][pos[1]] == "#":
            if delta[0] > 0:
                delta = [0,-1]
            elif delta[0] < 0:
                delta = [0,1]
            elif delta[1] > 0:
                delta = [1,0]
            else:
                delta = [-1,0]
            grid[pos[0]][pos[1]] = "."
        else:
            if delta[0] > 0:
                delta = [0,1]
            elif delta[0] < 0:
                delta = [0,-1]
            elif delta[1] > 0:
                delta = [-1,0]
            else:
                delta = [1,0]
            grid[pos[0]][pos[1]] = "#"
            infects += 1
        pos[0] += delta[0]
        pos[1] += delta[1]
        if pos[0] < 0:
            grid.insert(0,["."]*len(grid[1]))
            pos[0] = 0
        elif pos[0] >= len(grid):
            grid.append(["."]*len(grid[1]))
        elif pos[1] >= len(grid[0]):
            for j in range(len(grid)):
                grid[j].append(".")
        elif pos[1] < 0:
            for j in range(len(grid)):
                grid[j].insert(0,".")
            pos[1] = 0
    return infects
def nodes_weak(grid, times):
    delta = [-1,0]
    infects = 0
    pos = [len(grid) // 2] * 2
    for i in range(times):
        if grid[pos[0]][pos[1]] == "#":
            if delta[0] > 0:
                delta = [0,-1]
            elif delta[0] < 0:
                delta = [0,1]
            elif delta[1] > 0:
                delta = [1,0]
            else:
                delta = [-1,0]
            grid[pos[0]][pos[1]] = "F"
        elif grid[pos[0]][pos[1]] == ".":
            if delta[0] > 0:
                delta = [0,1]
            elif delta[0] < 0:
                delta = [0,-1]
            elif delta[1] > 0:
                delta = [-1,0]
            else:
                delta = [1,0]
            grid[pos[0]][pos[1]] = "W"
        elif grid[pos[0]][pos[1]] == "F":
            if delta[0] > 0:
                delta = [-1,0]
            elif delta[0] < 0:
                delta = [1,0]
            elif delta[1] > 0:
                delta = [0,-1]
            else:
                delta = [0,1]
            grid[pos[0]][pos[1]] = "."
        else:
            infects += 1
            grid[pos[0]][pos[1]] = "#"
        pos[0] += delta[0]
        pos[1] += delta[1]
        if pos[0] < 0:
            grid.insert(0,["."]*len(grid[1]))
            pos[0] = 0
        elif pos[0] >= len(grid):
            grid.append(["."]*len(grid[1]))
        elif pos[1] >= len(grid[0]):
            for j in range(len(grid)):
                grid[j].append(".")
        elif pos[1] < 0:
            for j in range(len(grid)):
                grid[j].insert(0,".")
            pos[1] = 0
    return infects

answer_one = str(nodes(deepcopy(content),10000))
answer_two = str(nodes_weak(deepcopy(content),10000000))

print("p1: " + answer_one)
print("p2: " + answer_two)
