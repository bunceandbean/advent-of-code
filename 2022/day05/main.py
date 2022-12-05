import re
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

stacks = ['LNWTD','CPH','WPHNDGMJ','CWSNTQL','PHCN','THNDMWQB','MBRJGSL','ZNWGVBRT','WGDNPL']

def crate_move(stacks, in_order):
    stacks = [list(x) for x in stacks]
    for line in content[10:]:
        num,here,there = map(int, re.findall(r'\d+', line))
        to_add = []
        for _ in range(num):
            ch = stacks[here-1].pop(~0)
            if in_order:
                to_add.append(ch)
            else:
                stacks[there-1].append(ch)
        if in_order:
            stacks[there-1] += to_add[::-1]
    out_str = ""
    for stack in stacks:
        out_str += stack.pop(~0)
    return out_str

answer_one = crate_move(stacks, False)
answer_two = crate_move(stacks, True)
print("p1:", answer_one)
print("p2:", answer_two)
