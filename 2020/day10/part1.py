answer = 0
# Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
content.append(0)
content.sort()


def findRoute():
    oneCount = 0
    threeCount = 0
    for i in range(len(content)-1):
        diff = content[i+1] - content[i]
        if diff == 1:
            oneCount += 1
        elif diff == 3:
            threeCount += 1
    return (threeCount + 1) * oneCount

answer = findRoute()
print(answer)
