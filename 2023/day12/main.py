from cachetools import cached
from cachetools.keys import hashkey

bin_map = {
    '#' : 1,
    '.' : 0,
    '?' : -1
}


with open("input.txt") as f:
    content =  [x.split(" ") for x in f.read().split("\n")[:~0]]
    rows = [(tuple(map(lambda n: bin_map[n], x[0])), tuple(map(int, x[1].split(",")))) for x in content]
    rows_p2 = []
    for row in rows:
        nums = row[0]
        rules = row[1]
        for i in range(4):
            nums += tuple([-1])
            nums += nums
            rules += rules
        rows_p2.append((nums, rules))

def check_match(seq, rules):
    str_seq = "0" + "".join(map(str, seq)) + "0"
    seq = 0
    chains = []
    for ch in str_seq:
        if ch == "1":
            seq += 1
        else:
            if seq:
                chains.append(seq)
                seq = 0 
    return tuple(chains) == rules[:len(chains)]

total = 0
@cached(cache={}, key=lambda line, rules, i : hashkey(line, rules))
def check_valid(line, rules, i):
    if i != 0 and not check_match(line[:i], rules):
        return 0
    try:
        next_i = line[i:].index(-1) + i
    except ValueError:
        if check_match(line, rules):
            return 1
        return 0
    new_line_0 = line[:next_i] + tuple([0]) + line[next_i+1:]
    new_line_1 = line[:next_i] + tuple([1]) + line[next_i+1:]
    return check_valid(new_line_0, rules, next_i) + check_valid(new_line_1, rules, next_i)

for row in rows:
    total += check_valid(row[0], row[1], 0)

print(total)