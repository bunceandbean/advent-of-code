from collections import Counter
import random
answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

ranges = []
matching_ranges = []
valid_ticks = []
my_ticket = content[content.index("your ticket:") +1]
my_ticket = my_ticket.split(",")
for num in my_ticket:
    my_ticket[my_ticket.index(num)] = int(num)

def mode(list):
    c = Counter(list)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

def valid_num(num):
    rate = 0
    amt_range = 0
    for range in ranges:
        if int(num) < range[1] and int(num) > range[0]:
            amt_range += 1
    if amt_range != 0:
        return True
    return False

for line in content:
    if "-" in line:
        r1 = line[line.index(":")+2:line.index(" or")]
        r1 = [int(r1[:r1.index("-")]),int(r1[r1.index("-")+1:])]
        r2 = line[line.index(" or")+4:]
        r2 = [int(r2[:r2.index("-")]),int(r2[r2.index("-")+1:])]
        ranges.append(r1)
        ranges.append(r2)
        matching_ranges.append([r1,r2])

content = content[content.index("nearby tickets:")+1:]

for line in content:
    line = line.split(",")
    valid = True
    for num in line:
        if not(valid_num(num)):
            valid = False
    if valid:
        valid_ticks.append(line)
key = {}
for ranges in matching_ranges:
    outlines = []
    for ticket in valid_ticks:
        outline = []
        for i in range(20):
            num = int(ticket[i])
            if (num <= int(ranges[0][1]) and num >= int(ranges[0][0])) or (num >= int(ranges[1][0]) and num <= int(ranges[1][1])):
                outline.append("Y")
            else:
                outline.append("N")
        outlines.append(outline)
    for i in range(20):
        total = 0
        for poss in outlines:
            if poss[i] == "Y":
                total += 1
        if total == len(valid_ticks):
            if matching_ranges.index(ranges) in key:
                key[matching_ranges.index(ranges)].append(i)
            else:
                key[matching_ranges.index(ranges)] = [i]


new_key = {}
ignore = []
while len(new_key) < 20:
    for i in range(20):
        if len(key[i]) == 1:
            new_key[i] = key[i][0]
            ignore.append(key[i][0])
        else:
            one = []
            for j in key[i]:
                if j not in ignore:
                    one.append(j)

            if len(one) == 1:
                new_key[i] = one[0]
                ignore.append(one[0])

mult = 1
for i in range(6):
    mult *= my_ticket[new_key[i]]
answer = mult
print(answer)
