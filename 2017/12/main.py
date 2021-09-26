#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]
    
groups = []
flat_groups = []
for num in range(len(content)):
    if num in flat_groups:
        continue
    num_group = [num]
    cur_length = 0
    while len(num_group) != cur_length:
        cur_length = len(num_group)
        for program in content:
            prog_num = int(program[:program.index("<")-1])
            pipes = list(map(int,program[program.index(">")+2:].split(", ")))
            if prog_num in flat_groups:
                continue
            for progs in num_group:
                if progs in pipes and prog_num not in num_group:
                    num_group.append(prog_num)
                    flat_groups.append(prog_num)
                    break
    groups.append(num_group)


answer_one = str(len(groups[0]))
answer_two = str(len(groups))
print("p1: " + answer_one)
print("p2: " + answer_two)
