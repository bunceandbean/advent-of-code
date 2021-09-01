answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def getRibbon(l,w,h):
    sides = [l+w,w+h,h+l]
    sides.sort()
    return 2*sides[0] + getVol(l,w,h)

def getVol(l,w,h):
    return l*w*h

totalRibbon = 0
for dimension in content:
    l = int(dimension[:dimension.index("x")])
    w = int(dimension[dimension.index("x") + 1:][:dimension[dimension.index("x") + 1:].index("x")])
    h = int(dimension[dimension.index("x") + 1:][dimension[dimension.index("x") + 1:].index("x")+1:])
    totalRibbon += getRibbon(l,w,h)

answer = totalRibbon
print(answer)
