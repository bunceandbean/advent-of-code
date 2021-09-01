answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def findRow(partition):
    range = [0,127]
    for half in partition:
        if half == "F":
            range[1] = range[1] - (range[1] + 1 - range[0])/2
        else:
            range[0] = range[0] + (range[1] + 1 - range[0])/2
    return int(range[0]) #doesnt matter which one is returned

def findCol(partition):
    range = [0,7]
    for half in partition:
        if half == "L":
            range[1] = range[1] - (range[1] + 1 - range[0])/2
        else:
            range[0] = range[0] + (range[1] + 1 - range[0])/2
    return int(range[0]) #doesnt matter which one is returned

seatIDS = []
for seat in content:
    partition = seat[:7]
    row = findRow(partition)
    partition = seat[7:]
    col = findCol(partition)
    id = row * 8 + col
    seatIDS.append(id)

answer = max(seatIDS)
print(answer)
