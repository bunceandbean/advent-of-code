import re
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def check_regex(lines):
    return sum(len(re.findall("XMAS", x)) + len(re.findall("SAMX", x)) for x in lines)

def part1():
    cols = ["".join([x[i] for x in content]) for i in range(len(content[0]))]
    diag_up = []
    diag_down = []
    cur_ups = ["",""]
    cur_downs = ["",""]
    for i in range(len(content)):
        x = i
        y = 0
        while x in range(len(content)) and y in range(len(content)):
            cur_ups[0] += content[x][y]
            cur_ups[1] += content[len(content)-y-1][len(content)-x-1]
            cur_downs[0] += content[len(content)-y-1][x]
            cur_downs[1] += content[x][len(content)-y-1]
            x -= 1
            y += 1
        diag_up += cur_ups if i < len(content) - 1 else [cur_ups[0]]
        diag_down += cur_downs if i < len(content) - 1 else [cur_downs[0]]
        cur_ups = ["",""]
        cur_downs = ["",""]
    return sum(map(check_regex, [content,cols,diag_down,diag_up]))

def part2():
    total = 0
    mas = ["MAS","SAM"]
    for r in range(len(content)-2):
        t,m,b = r, r+1, r+2
        print(t,m,b)
        for i in range(len(content)-2):
            if (content[t][i] + content[m][i+1] + content[b][i+2] in mas) and (content[t][i+2] + content[m][i+1] + content[b][i] in mas):
                total += 1
    return total
                
print("p1:", part1())
print("p2:", part2())