from itertools import combinations
with open("input.txt") as f:
    content = f.read().split("\n")
    nums = [int(x) for x in content[:len(content)-1]]

combs = 0
min_combs = 0
min_len = 100
for i in range(len(nums)):
    for comb in list(combinations(nums,i)):
        if sum(comb) == 150:
            combs += 1
            if len(comb) < min_len:
                min_len = len(comb)
                min_combs = 0
            if len(comb) == min_len:
                min_combs += 1

answer_one = str(combs)
answer_two = str(min_combs)
print("p1: " + answer_one)
print("p2: " + answer_two)
