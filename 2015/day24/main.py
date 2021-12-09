from itertools import combinations
from math import prod

with open("input.txt") as f:
    content = list(map(int,f.read().split("\n")[:~0]))

def balance(groups):
    for i in range(1,len(content)-1):
        g_1 = [x for x in list(combinations(content,i)) if sum(x) == sum(content)/groups]
        if len(g_1) > 0:
            break
    return g_1

answer_one = prod(min(balance(3), key=lambda x: prod(x)))
answer_two = prod(min(balance(4), key=lambda x: prod(x)))
print("p1:",answer_one)
print("p2:",answer_two)
