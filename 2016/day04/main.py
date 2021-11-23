import string
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
alpha = list(string.ascii_lowercase)


def checks(line):
    freq = []
    checksum = ""
    model = line[line.index('[')+1:len(line)-1]
    for i in range(len(alpha)):
        freq.append(line.count(alpha[i]))
    for i in range(max(freq),0,-1):
        for j in range(len(freq)):
            if freq[j] == i:
                if len(checksum) >= 5:
                    return checksum == model
                checksum += alpha[j]
    return checksum == model

total = 0
valid = []
for line in content:
    if checks(line):
        valid.append(line)
        total += int(line[line.index("[")-3:line.index("[")])

north_id = 0
for line in valid:
    id = int(line[line.index("[")-3:line.index("[")])
    shift = id % 26
    message = ""
    for char in line:
        if char in alpha:
            message += alpha[(alpha.index(char) + shift) % 26]
        elif char == "-":
            message += " "
        else:
            break
    if "north" in message:
        north_id = id

answer_one = str(total)
answer_two = str(north_id)
print("p1: " + answer_one)
print("p2: " + answer_two)
