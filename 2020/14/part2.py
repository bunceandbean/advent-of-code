import math
import random
answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

mask = ""
memory = {}

for line in content:
    if "mask" in line:
        mask = line[7:]
    else:
        mem_index = format(int(line[line.index("[")+1:line.index("]")]), '036b')
        mem_num = int(line[line.index("=") + 2:])
        mem_index = list(mem_index)
        index_list = []
        i = 0
        x_count = 0
        for bit in mask:
            if bit == "1":
                mem_index[i] = bit
            if bit == "X":
                index_list.append(i)
                x_count += 1
            i += 1
        mem_fill = []
        while len(mem_fill) < math.pow(2,x_count):
            for num in index_list:
                mem_index[num] = str(random.randint(0, 1))
            if int("".join(mem_index),2) not in mem_fill:
                mem_fill.append(int("".join(mem_index),2))
        for index in mem_fill:
            memory[index] = mem_num
answer = 0
for num in memory:
    answer += memory[num]

print(answer)
