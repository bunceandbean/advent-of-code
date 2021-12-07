with open("input.txt") as f:
    content = [*eval(f.read().split("\n")[:~0][0])]

def fuel(expense):
    best = 100000000
    for x in range(max(content)):
        sums = 0
        for m in content:
            sums += sum({*range(abs(m-x)+1)}) if expense else abs(m-x)
        best = sums if sums < best else best
    return best
    
answer_one = str(fuel(False))
answer_two = str(fuel(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
