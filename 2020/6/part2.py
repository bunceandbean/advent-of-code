answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0
allChars = []
alph = "abcdefghijklmnopqrstuvwxyz"
for person in content:
    if person != "":
        tempList = []
        for char in person:
            tempList.append(char)
        allChars.append(tempList)
    else:
        for char in alph:
            charCount = 0
            for list in allChars:
                if char in list:
                    charCount += 1
            if charCount == len(allChars):
                total +=1
        allChars = []


answer = total
print(answer)
