answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read()

floor = 0
for level in content:
    if level == "(":
        floor += 1
    else:
        floor -= 1

answer = floor
print(answer)
