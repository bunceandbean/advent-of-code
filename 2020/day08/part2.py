answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def loop(content):
    acc = 0
    beenHere = []
    count = 0
    while count < len(content):
        if count in beenHere:
            acc = 0
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
    return acc
pos = 0
for thing in content:
    tempCon = content.copy()
    if thing[0:3] == "nop":
        tempCon[pos] = "jmp" + tempCon[pos][3:]
    elif thing[0:3] == "jmp":
        tempCon[pos] = "nop" + tempCon[pos][3:]
    if thing[0:3] != "acc":
        if loop(tempCon) != 0:
            answer = loop(tempCon)
    pos += 1


print(answer)
