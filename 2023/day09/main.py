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
        
    
print("p1:", find_next_num(False))
print("p2:", find_next_num(True))
