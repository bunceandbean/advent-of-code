import re
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

stacks = ['LNWTD','CPH','WPHNDGMJ','CWSNTQL','PHCN','THNDMWQB','MBRJGSL','ZNWGVBRT','WGDNPL']

def crate_move(stacks, in_order):
    stacks = [list(x) for x in stacks]
    for line in content[10:]:
        num,here,there = map(int, re.findall(r'\d+', line))
        stacks[there-1] += [stacks[here-1].pop() for _ in range(num)][::-1 if in_order else 1]
    return "".join(stack.pop() for stack in stacks)

answer_one = crate_move(stacks, False)
answer_two = crate_move(stacks, True)
print("p1:", answer_one)
print("p2:", answer_two)
