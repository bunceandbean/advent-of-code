from random import randint
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

boss = [int(content[x][content[x].index(":")+2:]) for x in range(len(content))]
wiz = [50,500,0]

moves = {
"Magic Missile":{"cost":53,"dmg":4,"heal":0,"arm":0,"mana":0,"tick":1},
"Drain":{"cost":73,"dmg":2,"heal":2,"arm":0,"mana":0,"tick":1},
"Shield":{"cost":113,"dmg":0,"heal":0,"arm":7,"mana":0,"tick":6},
"Poison":{"cost":173,"dmg":3,"heal":0,"arm":0,"mana":0,"tick":6},
"Recharge":{"cost":229,"dmg":0,"heal":0,"arm":0,"mana":101,"tick":5}
}

def tick(fxs,wiz,boss):
    rm = []
    for fx in fxs:
        fxs[fx] -= 1
        boss[0] -= moves[fx]["dmg"]
        wiz[0] += moves[fx]["heal"]
        wiz[1] += moves[fx]["mana"]
        if fx == "Shield":
            wiz[2] = moves[fx]["arm"]
        if fxs[fx] <= 0:
            if fx == "Shield":
                wiz[2] = 0
            rm.append(fx)
    for out in rm:
        del fxs[out]
    return [fxs,wiz,boss]


def battle(wiz,boss,hard):
    min_mana = 10000
    w_t = wiz.copy()
    b_t = boss.copy()
    choose = [*moves.keys()]
    costs = [moves[x]["cost"] for x in moves]
    for i in range(10000000):
        mana = 0
        fxs = {}
        wiz,boss = w_t.copy(),b_t.copy()
        while True:
            if wiz[1] < min(costs) <= 0 or wiz[0] <= 0:
                break
            move = choose[randint(0,len(choose)-1)]
            tmp = tick(fxs.copy(),wiz.copy(),boss.copy())
            wiz = tmp[1].copy()
            boss = tmp[2].copy()
            fxs = tmp[0].copy()
            if wiz[1] < min(costs) or wiz[0] <= 0:
                break
            while move in fxs and moves[move]["cost"] > wiz[1]:
                move = choose[randint(0,len(choose)-1)]
            mana += moves[move]["cost"]
            wiz[1] -= moves[move]["cost"]
            if hard:
                wiz[0] -= 1
            if wiz[0] <= 0:
                break
            if boss[0] <= 0 and mana < min_mana:
                min_mana = mana
                break
            fxs[move] = moves[move]["tick"]
            tmp = tick(fxs.copy(),wiz.copy(),boss.copy())
            wiz = tmp[1].copy()
            if wiz[0] <= 0:
                break
            if boss[0] <= 0 and mana < min_mana:
                min_mana = mana
                break
            boss = tmp[2].copy()
            fxs = tmp[0].copy()
            if wiz[1] < min(costs) or wiz[0] <= 0:
                break
            if boss[0] <= 0 and mana < min_mana:
                min_mana = mana
                break
            wiz[0] -= (boss[1] - wiz[2])

    return min_mana



answer_one = battle(wiz.copy(),boss.copy(),False)
answer_two = battle(wiz.copy(),boss.copy(),True)
print("p1:",answer_one)
print("p2:",answer_two)
