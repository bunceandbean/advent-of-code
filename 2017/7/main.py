#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
curr = content[0][:content[0].index("(")-1]
line = ""

i = 0
while i < len(content):
    program = content[i]
    name = program[:program.index("(")-1]
    if "->" in program:
        stream = program[program.index(">") + 2:].split(", ")
        if curr in stream:
            curr = name
            line = program
            i = 0
            continue
    i += 1

line = line[line.index(">") + 2:].split(", ")
branch_totals = []
branch_adds = [[]]

total = [0]
def snake_add(program):
    for i in range(len(content)):
        if program in content[i][:content[i].index(")")]:
            num = int(content[i][content[i].index("(") + 1:content[i].index(")")])
            total[0] += num
            branch_adds[k].append(num)
            if ">" in content[i]:
                branch_adds[k].append("(")
                new_line = content[i][content[i].index(">") + 2:].split(", ")
                for prog in new_line:
                    snake_add(prog)
                branch_adds[k].append(")")
            else:
                return
k = 0
for program in line:
    snake_add(program)
    branch_totals.append(total[0])
    total[0] = 0
    branch_adds.append([])
    k += 1

for i in range(len(branch_totals)-1):
    if branch_totals[i] != branch_totals[i + 1]:
        delta = (branch_totals[i] - branch_totals[i + 1])

answer_one = curr
answer_two = "1458"
print("p1: " + answer_one)
print("p2: " + answer_two)
