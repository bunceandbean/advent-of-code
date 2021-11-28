with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[0:~0]

def signal(content):
    row_num = len(content[0])
    high = ""
    low = ""
    for i in range(row_num):
        ascii = []
        for j in range(len(content)):
            ascii.append(ord(content[j][i]))
        high += chr(max(set(ascii), key=ascii.count))
        low += chr(min(set(ascii), key=ascii.count))
    return [low, high]

answer_one = signal(content)[1]
answer_two = signal(content)[0]
print("p1: " + answer_one)
print("p2: " + answer_two)
