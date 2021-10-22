#Open file and compress contents into an array
with open("input.txt") as f:
    content = f.read().split("\n")
    content = [list(x) for x in content][:len(content)-2]
x = content[0].index("|")
y = 0
dx = 0
dy = 1
combos = [[-1,0],[1,0],[0,1],[0,-1]]
steps = 0
last = ""
letters = ""

while x >= 0 and y >= 0 and content[y][x] != " ":
    steps += 1
    cur = content[y][x]
    if content[y][x].isalpha():
        letters += content[y][x]
    elif content[y][x] == "+":
        pos = []
        for combo in combos:
            try:
                if content[y+combo[1]][x+combo[0]] == last:
                    continue
                pos.append([content[y+combo[1]][x+combo[0]],combo])
            except:
                continue
        for p in pos:
            if p[0] != " ":
                dx = p[1][0]
                dy = p[1][1]
    x += dx
    y += dy
    last = cur

answer_one = letters
answer_two = str(steps)
print("p1: " + answer_one)
print("p2: " + answer_two)
