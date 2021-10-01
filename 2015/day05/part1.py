answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def vowelCheck(string):
    vowelCount = 0
    for char in string:
        if char in "aeiou":
            vowelCount += 1
    if vowelCount >= 3:
        return True
    return False

def repeatCheck(string):
    count = 0
    for char in string:
        if count != 0:
            if string[count - 1] == char:
                return True
        count += 1
    return False

def notString(string):
    notIn = ["ab","cd","pq","xy"]
    for comb in notIn:
        if comb in string:
            return False
    return True


def isNice(string):
    if notString(string) and repeatCheck(string) and vowelCheck(string):
        return True
    return False


totalNice = 0
for string in content:
    if isNice(string):
        totalNice += 1

answer = totalNice
print(answer)
