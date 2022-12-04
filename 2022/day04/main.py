with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

subsets = 0
overlap = 0
for line in content:
    a,b = int(line[:line.index("-")]), int(line[line.index("-")+1:line.index(",")])
    range_two = line[line.index(",")+1:]
    c,d = int(range_two[:range_two.index("-")]), int(range_two[range_two.index("-")+1:])
    set_1,set_2, = set(range(a,b+1)), set(range(c,d+1))
    if set_1 | set_2 in (set_1,set_2):
        subsets += 1
    if set_1 & set_2 or set_1 & set_2:
        overlap += 1

answer_one = subsets
answer_two = overlap
print("p1:", answer_one)
print("p2:", answer_two)
