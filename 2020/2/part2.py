answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for string in content:
    valid = False
    deltaChar = string[string.index(" ") + 1 : string.index(" ")+2]
    pos1Char = int(string[:string.index("-")])-1
    pos2Char = int(string[string.index("-")+1:string.index(" ")])-1
    password = string[string.index(": ")+2:]

    if password[pos1Char] == deltaChar:
        valid = not valid
    if password[pos2Char] == deltaChar:
        valid = not valid
    if valid:
        answer += 1

print(answer)
