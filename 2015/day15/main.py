with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]


def get_score(amts):
    running = 1
    len_key = list(items.keys())[0]
    for i in range(len(items[len_key])):
        total = 0
        for key in amts.keys():
            total += amts[key]*items[key][i]
        if total < 0:
            return 0
        running *= total
    return running


items = {}
amts = {}
cals = []
for line in content:
    ingred = line[:line.index(":")]
    items[ingred] = []
    amts[ingred] = 0
    arr = line[line.index(":")+1:].split(",")
    for des in arr:
        if "calories" not in des:
            items[ingred].append(int(des[des[1:].index(" ")+1:]))
        else:
            cals.append(int(des[des.index("calories") + 9:]))

highscore = 0
cal_500 = 0
for o in range(50):
    total_cals = 0
    amts[list(amts.keys())[0]] = o
    for t in range(50):
        amts[list(amts.keys())[1]] = t
        for th in range(50):
            amts[list(amts.keys())[2]] = th
            for f in range(50):
                total_cals = f*cals[3] + th*cals[2] + t*cals[1] + o*cals[0]
                amts[list(amts.keys())[3]] = f
                if sum(list(amts.values())) == 100:
                    score = get_score(amts)
                    if score > highscore:
                        highscore = score
                    if total_cals == 500 and score > cal_500:
                        cal_500 = score

answer_one = str(highscore)
answer_two = str(cal_500)
print("p1: " + answer_one)
print("p2: " + answer_two)
