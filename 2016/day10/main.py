with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def balance(out):
    bots = {}
    outputs = {}
    first = True
    while True:
        for line in content:
            try:
                bot = int(line[line.index("bot")+4:])
            except:
                bot = int(line[line.index("bot")+4:line.index("g")-1])
            if "goes" in line and first:
                val = int(line[line.index(" ")+1:line.index("goes")-1])
                if bot in bots:
                    bots[bot].append(val)
                else:
                    bots[bot] = [val]
            elif bot in bots and len(bots[bot]) == 2 and "goes" not in line:
                scope = line[line.index("to")+3:]
                low = int(scope[scope.index(" ")+1:scope.index("and")-1])
                high_scope = scope[scope.index("high")+8:]
                high = int(high_scope[high_scope.index(" ")+1:])
                if min(bots[bot]) == 17 and max(bots[bot]) == 61 and not out:
                    return bot
                if scope[0] == "o":
                    try:
                        outputs[low].append(min(bots[bot]))
                    except:
                        outputs[low] = [min(bots[bot])]
                else:
                    try:
                        bots[low].append(min(bots[bot]))
                    except:
                        bots[low] = [min(bots[bot])]
                if high_scope[0] == "o":
                    try:
                        outputs[high].append(max(bots[bot]))
                    except:
                        outputs[high] = [max(bots[bot])]
                else:
                    try:
                        bots[high].append(max(bots[bot]))
                    except:
                        bots[high] = [max(bots[bot])]
                bots[bot] = []
                if out:
                    try:
                        return outputs[0][0] * outputs[1][0] * outputs[2][0]
                    except:
                        pass
        first = False

answer_one = str(balance(False))
answer_two = str(balance(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
