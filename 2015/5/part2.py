answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def repeatCheck(string):
    count = 0
    for char in string:
        if count < len(string) - 2:
            if string[count + 2] == char:
                return True
        count += 1
    return False

def doubleRepeat(string):
    count = 0
    for char in string:
        if count != len(string) - 1:
            if char + string[count + 1] in string[count + 2 :]:
                return True
        count += 1
    return False

def isNice(string):
    if doubleRepeat(string) and repeatCheck(string):
        return True
    return False


totalNice = 0
for string in content:
    if isNice(string):
        totalNice += 1

answer = totalNice
print(answer)
