answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

acc = 0
beenHere = []
count = 0
while True:
    if count in beenHere:
        break
    else:
        beenHere.append(count)
        instruction = content[count][:content[count].index(" ")]
        if instruction == "nop":
            count +=1
            continue
        elif instruction == "acc":
            num = content[count][content[count].index(" ") + 1:]
            count += 1
            if num[0] == "-":
                acc -= int(num[1:])
            else:
                acc += int(num[1:])
        elif instruction == "jmp":
            num = content[count][content[count].index(" ") + 1:]
            if num[0] == "-":
                count -= int(num[1:])
            else:
                count += int(num[1:])

answer = acc
print(answer)
