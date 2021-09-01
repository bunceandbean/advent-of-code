import math
# Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
content.append(0)
content.sort()

print(max(content)+3)
print(math.factorial(21))
