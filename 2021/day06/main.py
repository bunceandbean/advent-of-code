with open("input.txt") as f:
    file = list(eval(f.read()))
    content = [file.count(x) for x in range(9)]

def lantern(amt,content):
    for i in range(amt):
        app = content.pop(0)
        content[6] += app
        content.append(app)
    return sum(content)

answer_one = str(lantern(80,content.copy()))
answer_two = str(lantern(256,content.copy()))
print("p1: " + answer_one)
print("p2: " + answer_two)
