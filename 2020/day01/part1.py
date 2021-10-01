answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

#for loop checking for condition
for num in content:
    for deltaNum in content:
        if num + deltaNum == 2020:
            answer = num*deltaNum
print(answer)
