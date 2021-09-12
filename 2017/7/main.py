#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
curr = content[0][:content[0].index("(")-1]

i = 0
while i < len(content):
    program = content[i]
    name = program[:program.index("(")-1]
    if "->" in program:
        stream = program[program.index(">") + 2:].split(", ")
        if curr in stream:
            curr = name
            i = 0
            continue
    i += 1

answer_one = curr
print("p1: " +  answer_one)
