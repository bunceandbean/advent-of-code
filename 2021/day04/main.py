with open("input.txt") as f:
    content = f.read().split("\n\n")[:~0]
    nums = [int(x) for x in content[0].split(",")]
    bingo = list(map(lambda x: [list(map(int,m.strip(",").split(","))) for m in x], \
    [x.replace("  "," 0").replace(' ',',').split("\n") for x in content[2:]]))
    wins = [bingo[i] + [list(x) for x in list(zip(*bingo[i]))] for i in range(len(bingo))]


def play(last):
    lst = []
    won = set()
    cur = (0,0)
    for num in nums:
        lst.append(num)
        for board in wins:
            for win in board:
                if all(x in lst for x in win):
                    pts = sum(set([m for x in board for m in x if m not in lst]))
                    if not last:
                        return lst[~0]*pts
                    cur = (pts,lst[~0]) if wins.index(board) not in won else cur
                    won.add(wins.index(board))
    return cur[0]*cur[1]


answer_one = str(play(False))
answer_two = str(play(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
