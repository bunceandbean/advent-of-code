answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

#Loop and count trees
slope = 0
treeCount = 0
for mapLine in content:
    if slope >= len(mapLine):
        slope = slope - len(mapLine)
    if mapLine[slope] == "#":
        treeCount += 1
    slope += 3

answer = treeCount
print(answer)
