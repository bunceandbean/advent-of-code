answer = 0
# Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

for i in range(25,len(content)):
    valid = False
    for num in content[i-25:i]:
        for j in range(0,25):
            if num + content[i-25:i][j] == content[i] and content[i-25:i][j] != num:
                valid = True
    if not valid:
        answer = content[i]

print(answer)
