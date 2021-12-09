with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def assembly(a,b):
    i = 0
    regs = {"a":a,"b":b}
    while i < len(content):
        reg = content[i]
        if "hlf" in reg:
            regs[reg[reg.index(" ")+1:]] //= 2
        elif "tpl" in reg:
            regs[reg[reg.index(" ")+1:]] *= 3
        elif "inc" in reg:
            regs[reg[reg.index(" ")+1:]] += 1
        elif "jmp" in reg:
            i += int(reg[reg.index(" ")+1:])
            continue
        elif "jie" in reg:
            if regs[reg[reg.index(" ")+1:reg.index(",")]] % 2 == 0:
                i += int(reg[reg.index(",")+2:])
                continue
        else:
            if regs[reg[reg.index(" ")+1:reg.index(",")]] == 1:
                i += int(reg[reg.index(",")+2:])
                continue
        i += 1
    return regs['b']

answer_one = assembly(0,0)
answer_two = assembly(1,0)
print("p1:",answer_one)
print("p2:",answer_two)
