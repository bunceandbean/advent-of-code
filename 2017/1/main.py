answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = content[0]

sum = 0
for i in range(len(content)):
    num = int(content[i])
    if i != len(content)-1:
        posNext = i + 1
    else:
        posNext = 0
    if num == int(content[posNext]):
        sum += num

answer = sum
print("p1: " + str(answer))
##########################################
new_sum = 0
for i in range(len(content)):
    num = int(content[i])
    posNext = (i + len(content)//2) % len(content)
    if num == int(content[posNext]):
        new_sum += num
answer = new_sum
print("p2: " + str(answer))
