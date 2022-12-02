with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

score = 0
lose = {"X":"B","Y":"C","Z":"A"}
win = {"Y":"A","Z":"B","X":"C"}

lose_me = {"B":"X","C":"Y","A":"Z"}
win_me = {"A":"Y","B":"Z","C":"X"}
draw = {"A":"X","B":"Y","C":"Z"}

for item in content:
    if item[2] == "X":
        score += 1
    elif item[2] == "Y":
        score += 2
    elif item[2] == "Z":
        score += 3
    if win[item[2]] == item[0]:
        score += 6
    elif lose[item[2]] == item[0]:
        score += 0
    else:
        score += 3
new_score = 0
for item in content:
    if item[2] == "X":
        my_item = lose_me[item[0]]
        if my_item == "X":
            new_score += 1
        elif my_item == "Y":
            new_score += 2
        elif my_item == "Z":
            new_score += 3
    elif item[2] == "Y":
        my_item = draw[item[0]]
        if my_item == "X":
            new_score += 1
        elif my_item == "Y":
            new_score += 2
        elif my_item == "Z":
            new_score += 3
        new_score += 3
    elif item[2] == "Z":
        my_item = win_me[item[0]]
        if my_item == "X":
            new_score += 1
        elif my_item == "Y":
            new_score += 2
        elif my_item == "Z":
            new_score += 3
        new_score += 6
answer_one = score
answer_two = new_score
print("p1:", answer_one)
print("p2:", answer_two)
