from collections import Counter
from collections import defaultdict
from copy import copy
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    poly = content[0]
    rules = {x[:x.index(' ')]: x[x.index('>')+2:] for x in content[2:]}

def chain(times,poly):
    count = Counter(poly)
    pairs = defaultdict(int)
    for i,j in zip(range(len(poly)-1),range(1,len(poly))):
        if poly[i] + poly[j] in rules:
            pairs[poly[i]+poly[j]] += 1
    for i in range(times):
        temp = copy(pairs)
        for pair in temp:
            if temp[pair] > 0:
                pairs[pair] -= temp[pair]
                pairs[rules[pair] + pair[1]] += temp[pair]
                pairs[pair[0] + rules[pair]] += temp[pair]
                count[rules[pair]] += temp[pair]
    return count.most_common()[0][1] - count.most_common()[~0][1]


answer_one = chain(10,poly)
answer_two = chain(40,poly)
print("p1:",answer_one)
print("p2:",answer_two)
