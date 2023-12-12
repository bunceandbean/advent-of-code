import numpy as np
with open("input.txt") as f:
    content = list(map(lambda x: list(map(int, x.split(" "))), f.read().split("\n")[:~0]))

def find_next_num(rev):
    next_total = 0
    for hist in content:
        diffs = hist[::-1] if rev else hist
        while diffs.count(0) != len(diffs):
            next_total += diffs[~0]
            diffs = [diffs[i] - diffs[i-1] for i in range(1,len(diffs))]
    return next_total

def lagrange(y, t):
    poly = 0
    x = [i for i in range(len(y))]
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        term = yi
        for j in range(len(x)):
             if i == j:
                continue
             term *= (t - x[j]) / (xi - x[j])
        poly += term
    return poly

def find_next_inter(rev):
    next_total = 0
    for hist in content:
        cur_hist = hist[::-1] if rev else hist
        next_total += lagrange(cur_hist, len(cur_hist))
    return round(next_total)

print("Normal Method:")
print("p1:", find_next_num(False))
print("p2:", find_next_num(True))

print("\nLagrange Method:")
print("p1:", find_next_inter(False))
print("p2:", find_next_inter(True))