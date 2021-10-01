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
        mem_index = int(line[line.index("[")+1:line.index("]")])
        mem_num = format(int(line[line.index("=") + 2:]), '036b')
        mem_num = list(mem_num)
        i = 0
        for bit in mask:
            if bit != "X":
                mem_num[i] = bit
            i += 1
        mem_num = "".join(mem_num)
        mem_num = int(mem_num,2)
        memory[mem_index] = mem_num
answer = 0
for num in memory:
    answer += memory[num]

print(answer)
