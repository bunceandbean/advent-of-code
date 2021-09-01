answer = 0
#Open file and compress lines into an string
with open("input.txt") as f:
    content = f.read()

xSanta = 0
ySanta = 0
xRobo = 0
yRobo = 0
coordList = []
turn = 0
for char in content:
    if char == "^":
        if turn % 2 == 0:
            ySanta += 1
        else:
            yRobo += 1
    if char == "v":
        if turn % 2 == 0:
            ySanta -= 1
        else:
            yRobo -= 1
    if char == ">":
        if turn % 2 == 0:
            xSanta += 1
        else:
            xRobo += 1
    if char == "<":
        if turn % 2 == 0:
            xSanta -= 1
        else:
            xRobo -= 1
    if turn % 2 == 0:
        coord = (xSanta,ySanta)
    else:
        coord = (xRobo,yRobo)
    if coord not in coordList:
        coordList.append(coord)
    turn += 1

answer = len(coordList)
print(answer)
