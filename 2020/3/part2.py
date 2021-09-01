answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

#Loop and count trees

def toboggan(slopeCount,skip):
    slope = 0
    treeCount = 0
    for mapLine in content:
        if(content.index(mapLine) % skip == 0):
            if slope >= len(mapLine):
                slope = slope - len(mapLine)
            if mapLine[slope] == "#":
                treeCount += 1
            slope += slopeCount

    return treeCount

answer = toboggan(1,1) * toboggan(3,1) * toboggan(5,1) * toboggan(7,1) * toboggan(1,2)
print(answer)
