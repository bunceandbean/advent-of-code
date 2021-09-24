#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read().strip().split(",")
dist = 0
coords = [0,0,0]
max_dist = 0
dirs = {
    "n":[0,1,-1],
    "ne":[1,0,-1],
    "nw":[-1,1,0],
    "s":[0,-1,1],
    "se":[1,-1,0],
    "sw":[-1,0,1]
}

for dir in content:
    abs_max = max([max(coords),min(coords)])
    for i in range(len(dirs[dir])):
        coords[i] += dirs[dir][i]
    if abs_max >= max_dist:
        max_dist = abs_max
        
if 0 in coords:
    for cord in coords:
        if cord != 0:
            dist = abs(cord)
else:
    dist = max([max(coords),min(coords)])

answer_one = str(dist)
answer_two = str(max_dist)
print("p1: " + answer_one)
print("p2: " + answer_two)
