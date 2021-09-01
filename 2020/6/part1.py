answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0
qCount = []
for person in content:
    if person != "":
        for char in person:
            if char not in qCount:
                qCount.append(char)
    else:
        total += len(qCount)
        qCount = []

answer = total
print(answer)
