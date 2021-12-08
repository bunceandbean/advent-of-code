from itertools import permutations
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

total = 0
t_sum = 0
for x in content:
    sums = ""
    guide = x[:x.index("|")-1].split(" ")
    out = x[x.index("|")+2:].split(" ")
    easy = [2,3,4,7]
    for num in out:
        if len(num) in easy:
            total += 1
    valid = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    found = {'a':'','b':'','c':'','d':'','e':'','f':'','g':''}
    perms = permutations([*found.keys()])
    for perm in perms:
        perm = iter(perm)
        for chr in found.keys():
            found[chr] = next(perm)
        ok = True
        for num in guide:
            build = ""
            for chr in num:
                build += found[chr]
            if "".join(sorted(build)) not in valid:
                ok = False
                break
        if ok:
            for num in out:
                build = ""
                for chr in num:
                    build += found[chr]
                sums += str(valid.index("".join(sorted(build))))
            t_sum += int(sums)

answer_one = total
answer_two = t_sum
print("p1:",answer_one)
print("p2:",answer_two)
