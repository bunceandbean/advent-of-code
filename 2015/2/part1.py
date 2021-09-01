answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def getSA(l,w,h):
    sides = [l*w,w*h,h*l]
    sides.sort()
    return 2*l*w + 2*w*h + 2*h*l + sides[0]

def getArea(a,b):
    return a*b
totalPaper = 0
for dimension in content:
    l = int(dimension[:dimension.index("x")])
    w = int(dimension[dimension.index("x") + 1:][:dimension[dimension.index("x") + 1:].index("x")])
    h = int(dimension[dimension.index("x") + 1:][dimension[dimension.index("x") + 1:].index("x")+1:])
    totalPaper += getSA(l,w,h)

answer = totalPaper
print(answer)
