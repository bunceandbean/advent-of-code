#Open file and compress content[i]s into an array
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]

ops = {
"set":"=",
"add": "+=",
"mul":"*=",
"mod": "%=",
}
def single_assembly():
    dex = 0
    while dex < len(content):
        cmd = content[dex][:3]
        var = content[dex][4:5]
        if var not in locals():
            exec(var + " = 0")
        if cmd in ops:
            val = content[dex][6:]
            exec(var + ops[cmd] + val)
        elif cmd == "snd":
            exec("snd" + ops["set"] + var)
        elif cmd == "jgz" and eval(var + "> 0"):
            val = content[dex][6:]
            dex += int(eval("val"))
            continue
        elif cmd == "rcv" and eval(var + "!= 0"):
            break
        dex += 1
    return eval("snd")

def duet_assembly():
    dex = [0,0]
    queue = [[],[]]
    pID = 0
    p1Vals = 0
    vars = [{"p":0},{"p":1}]
    swaps = False
    while True:
        cmd = content[dex[pID]][:3]
        var = content[dex[pID]][4:5]
        ####Check Vals###############
        if len(content[dex[pID]]) >= 7:
            val = content[dex[pID]][6:]
            if val.isdigit() or val[1:].isdigit():
                val = int(val)
            else:
                val = vars[pID][val]
        if var not in vars[pID]:
            vars[pID][var] = 0
        ##############################
        if cmd == "set":
            vars[pID][var] = val
        elif cmd == "add":
            vars[pID][var] += val
        elif cmd == "mul":
            vars[pID][var] *= val
        elif cmd == "mod":
            vars[pID][var] %= val
        elif cmd == "jgz":
            if var.isdigit() or var[1:].isdigit():
                jgzVal = int(var)
            else:
                jgzVal = vars[pID][var]
            if jgzVal > 0:
                dex[pID] += val
                continue
        elif cmd == "snd":
            queue[(pID + 1) % 2].append(vars[pID][var])
            if pID == 1:
                p1Vals += 1
        elif len(queue[pID]) > 0:
            vars[pID][var] = queue[pID].pop(0)
        else:
            pID = (pID + 1) % 2
            if swaps:
                break
            swaps = True
            continue
        swaps = False
        dex[pID] += 1
    return p1Vals

answer_one = str(single_assembly())
answer_two = str(duet_assembly())

print("p1: " + answer_one)
print("p2: " + answer_two)
