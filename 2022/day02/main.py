with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

map_1 = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3,
    "B X": 1,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2,
    "C Z": 3 + 3
}
map_2 = {
    "A X": 3,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2,
    "C Y": 3 + 3,
    "C Z": 1 + 6
}

score_1 = score_2 = 0
for item in content:
    score_1 += map_1[item]
    score_2 += map_2[item]

print("p1:", score_1)
print("p2:", score_2)
