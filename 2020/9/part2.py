answer = 0
# Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

def lookForRange(content):
    for i in range(2,len(content)):
        startIndex = 0
        endIndex = i
        while endIndex < len(content):
            if sum(content[startIndex:endIndex]) == 23278925:
                return max(content[startIndex:endIndex]) + min(content[startIndex:endIndex])
            startIndex += 1
            endIndex += 1


answer = lookForRange(content)
print(answer)
