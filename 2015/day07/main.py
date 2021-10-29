import numpy
from copy import deepcopy
with open("input.txt") as f:
    content = f.readlines()
    content = [x.strip("\n") for x in content]

reg = {}
for wire in content:
    if "AND" in wire:
        val1 = wire[:wire.index("AND")-1]
        val2 = wire[wire.index("AND")+4:wire.index("-")-1]
        if val1 not in reg and not val1.isdigit():
            reg[val1] = "NS"
        if val2 not in reg and not val2.isdigit():
            reg[val2] = "NS"
    elif "OR" in wire:
        val1 = wire[:wire.index("OR")-1]
        val2 = wire[wire.index("OR")+3:wire.index("-")-1]
        if val1 not in reg and not val1.isdigit():
            reg[val1] = "NS"
        if val2 not in reg and not val2.isdigit():
            reg[val2] = "NS"
    elif "LSHIFT" in wire or "RSHIFT" in wire:
        val1 = wire[:wire.index("SHIFT")-2]
        if val1 not in reg and not val1.isdigit():
            reg[val1] = "NS"
    elif "NOT" in wire:
        val1 = wire[wire.index("T")+2:wire.index("-")-1]
        if val1 not in reg and not val1.isdigit():
            reg[val1] = "NS"
    else:
        val1 = wire[:wire.index("-")-1]
        if val1 not in reg and not val1.isdigit():
            reg[val1] = "NS"
    val3 = wire[wire.index(">") + 2:]
    if val3 not in reg and not val3.isdigit():
        reg[val3] = "NS"

def circuit(reg,constant):
    comps = []
    if constant != 'None':
        con = reg[constant]
    while len(comps) < len(content):
        for wire in content:
            val3 = wire[wire.index(">") + 2:]
            in_comps = wire in comps
            if in_comps:
                continue
            if "AND" in wire:
                val1 = wire[0:wire.index("AND")-1]
                val2 = wire[wire.index("AND")+4:wire.index("-")-1]
                if val1.isdigit():
                    val1 = int(val1)
                else:
                    val1 = reg[val1]
                if val2.isdigit():
                    val2 = int(val2)
                else:
                    val2 = reg[val2]
                if val1 != "NS" and val2 != "NS":
                    reg[val3] = numpy.uint16(numpy.int16(val1 & val2))
                    comps.append(wire)
            elif "OR" in wire:
                val1 = wire[0:wire.index("OR")-1]
                val2 = wire[wire.index("OR")+3:wire.index("-")-1]
                if val1.isdigit():
                    val1 = int(val1)
                else:
                    val1 = reg[val1]
                if val2.isdigit():
                    val2 = int(val2)
                else:
                    val2 = reg[val2]
                if val1 != "NS" and val2 != "NS":
                    reg[val3] = numpy.uint16(numpy.int16(val1 | val2))
                    comps.append(wire)
            elif "LSHIFT" in wire or "RSHIFT" in wire:
                val1 = wire[0:wire.index("SHIFT")-2]
                val2 = int(wire[wire.index("T") + 2:wire.index("-")-1])
                if val1.isdigit():
                    val1 = int(val1)
                else:
                    val1 = reg[val1]
                if val1 != "NS" and "L" in wire:
                    reg[val3] = numpy.uint16(numpy.int16(val1 << val2))
                    comps.append(wire)
                elif val1 != "NS" and "R" in wire:
                    reg[val3] = numpy.uint16(numpy.int16(val1 >> val2))
                    comps.append(wire)
            elif "NOT" in wire:
                val1 = wire[wire.index("T")+2:wire.index("-")-1]
                if val1.isdigit():
                    val1 = int(val1)
                else:
                    val1 = reg[val1]
                if val1 != "NS":
                    reg[val3] = numpy.uint16(numpy.int16(~val1))
                    comps.append(wire)
            else:
                val1 = wire[:wire.index("-")-1]
                if val1.isdigit():
                    val1 = int(val1)
                else:
                    val1 = reg[val1]
                if val1 != "NS":
                    reg[val3] = val1
                    comps.append(wire)
            if constant != "None":
                reg[constant] = con
    return str(reg['a'])

answer_one = circuit(deepcopy(reg),"None")
reg['b'] = int(answer_one)
answer_two = circuit(deepcopy(reg),"b")

print("p1: " + answer_one)
print("p2: " + answer_two)
