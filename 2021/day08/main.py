with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

total = 0
out_sum = 0
for line in content:
    guide = line[:line.index("|")-1].split(" ")
    out = line[line.index("|")+2:].split(" ")
    easy = {2:1,3:7,4:4,7:8}
    maps = {(2,3,6):0,(1,2,5):2,(2,3,5):3,(1,3,5):5,(1,3,6):6,(2,4,6):9}
    for num in out:
        if len(num) in easy:
            total += 1
    route = ["" for x in range(10)]
    for signal in guide:
        if len(signal) in easy:
            route[easy[len(signal)]] = set(signal)
    for signal in guide:
        sig = set(signal)
        if sig not in route:
            r_1 = len(sig.intersection(route[1]))
            r_4 = len(sig.intersection(route[4]))
            route[maps[(r_1,r_4,len(signal))]] = sig
    out_sum += int("".join([str(route.index(set(signal))) for signal in out]))

answer_one = total
answer_two = out_sum
print("p1:",answer_one)
print("p2:",answer_two)
