#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
cpu_1 = content.copy()
cpu_2 = content.copy()

i = 0
steps = 0
while i >= 0 and i <= len(cpu_1) - 1:
    cpu_1[i] += 1
    i += cpu_1[i] - 1
    steps += 1
answer_one = steps

j = 0
steps = 0
while j >= 0 and j <= len(cpu_2) - 1:
    if cpu_2[j] >= 3:
        cpu_2[j] -= 1
        j += cpu_2[j] + 1
    else:
        cpu_2[j] += 1
        j += cpu_2[j] - 1
    steps += 1

answer_two = steps
print("p1: " + str(answer_one))
print("p2: " + str(answer_two))
