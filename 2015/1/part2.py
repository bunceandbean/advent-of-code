answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read()

floor = 0
basementPos = 0
index = 0
for level in content:
    if level == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        basementPos = index + 1
        break
    index += 1

answer = basementPos
print(answer)
