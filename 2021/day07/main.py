from statistics import median
from statistics import mean
with open("input.txt") as f:
    content = [*eval(f.read().split("\n")[:~0][0])]

def fuel(expense):
    med = int(median(content))
    mid = int(mean(content))
    return sum(map(lambda x:sum({*range(abs(x-mid)+1)}),content)) \
    if expense else sum(map(lambda x:abs(x-med),content))

answer_one = str(fuel(False))
answer_two = str(fuel(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
