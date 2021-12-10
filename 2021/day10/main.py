from statistics import median
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

weight = {")":3,"]":57,"}":1197,">":25137}
table = {"(":1,"[":2,"{":3,"<":4}
match = {")": "(", "]": "[", "}": "{", ">": "<"}

def corrupt(incomp):
    sums = 0
    scores = []
    for line in content:
        stack = []
        corrupt = False
        for chr in line:
            if chr not in weight:
                stack.append(chr)
            elif stack[~0] != match[chr]:
                corrupt = True
                sums += weight[chr]
                break
            else:
                stack.pop(~0)
        if incomp and not corrupt:
            score = 0
            stack.reverse()
            for chr in stack:
                score *= 5
                score += table[chr]
            scores.append(score)
    if not incomp:
        return sums
    else:
        return int(median(scores))



answer_one = corrupt(False)
answer_two = corrupt(True)
print("p1:",answer_one)
print("p2:",answer_two)
