answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for string in content:
    charCount = 0
    deltaChar = string[string.index(" ") + 1 : string.index(" ")+2]
    for char in string[string.index(": ")+2:]:
        if char == deltaChar:
            charCount += 1
    if charCount >= int(string[:string.index("-")]) and charCount <= int(string[string.index("-")+1:string.index(" ")]):
        answer += 1

print(answer)
