with open("input.txt") as f:
    content = [x.split("   ") for x in f.read().split("\n")[:~0]]
    left, right = sorted([int(x[0]) for x in content]), sorted([int(x[1]) for x in content])

total = sum([abs(left[i] - right[i]) for i in range(len(content))])
similar = sum([right.count(x) * x for x in left])

print("p1:", total)
print("p2:", similar)