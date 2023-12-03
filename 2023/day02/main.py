from aoc_util import *
import math

with open("input.txt") as f:
    content = f.read()
    result = cut_down(content, "rbg0123456789;\n:", "gr", "g")
    games = [x[x.index(":")+1:].split(";") for x in result]


color = ['r','g','b']
rule = [12,13,14]
sumd = 0
sump = 0
for i in range(len(games)):
    max_cols = [0,0,0]
    out = False
    for roll in games[i]:
        num = ""
        for ch in roll:
            if ch.isnumeric():
                num += ch
            else:
                if int(num) > rule[color.index(ch)]:
                        out = True
                if int(num) > max_cols[color.index(ch)]:
                    max_cols[color.index(ch)] = int(num)
                num = ""
    if not out:
        sumd += i + 1
    sump += math.prod(max_cols)

print("p1:", sumd)
print("p2:", sump)