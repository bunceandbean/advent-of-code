with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    content = [x.replace("  ", " ") for x in content]

muls = [1 for i in range(0, len(content))]
cards = len(content)
total = 0
for line in content:
    new_line = line[line.index(":") +2 :]
    nums = new_line.split("|")
    com = [list(map(int, num.strip(" ").split(" "))) for num in nums]
    match = 0
    new_cards = 0
    sumd = 0
    for n in com[1]:
        if n in com[0]:
            match += 1
            new_cards += 1
            muls[content.index(line) + match] += muls[content.index(line)]
            if sumd == 0:
                sumd = 1
            else:
                sumd *= 2
    total += sumd
    cards += new_cards * muls[content.index(line)]

print("p1:", total)
print("p2:", cards)
