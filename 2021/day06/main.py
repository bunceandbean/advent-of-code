with open("input.txt") as f:
    file = list(eval(f.read()))
    content = [file.count(x) for x in range(9)]

def lantern(amt,content):
    for i in range(amt):
        new = [0 for i in range(9)]
        for i in range(0,9):
            new[i] = content[(i+1)%9]
        new[6] += content[0]
        content = new.copy()
    return sum(content)

answer_one = str(lantern(80,content))
answer_two = str(lantern(256,content))
print("p1: " + answer_one)
print("p2: " + answer_two)
