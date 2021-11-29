with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[0:~0]

def auth(w,t):
    lcd = [[0 for x in range(w)] for y in range(t)]
    for rule in content:
        if "rect" in rule:
            l = int(rule[rule.index(" ")+1:rule.index("x")])
            h = int(rule[rule.index("x")+1:])
            for y in range(h):
                for x in range(l):
                    lcd[y][x] = 1
        elif "row" in rule:
            row = int(rule[rule.index("=")+1:rule.index("by")-1])
            shift = int(rule[rule.index("by") + 3:])
            dex = []
            for i in range(w):
                if lcd[row][i] == 1:
                    lcd[row][i] = 0
                    dex.append((i+shift)%w)
            for i in dex:
                lcd[row][i] = 1
        elif "column" in rule:
            col = int(rule[rule.index("=")+1:rule.index("by")-1])
            shift = int(rule[rule.index("by") + 3:])
            dex = []
            for i in range(t):
                if lcd[i][col] == 1:
                    lcd[i][col] = 0
                    dex.append((i+shift)%t)
            for i in dex:
                lcd[i][col] = 1
    return [sum([sum(x) for x in lcd]), lcd]

answer = auth(50,6)
answer_one = str(answer[0])
answer_two = "\n".join(["".join([str(i) for i in x]) for x in answer[1]]).replace("0"," ")
print("p1: " + answer_one)
print("p2: " + "\n" +  answer_two)
