from string import ascii_lowercase
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read().strip().split(",")

programs = list(ascii_lowercase[:16])

def find_cycle(programs):
    orns = ["".join(programs)]
    while True:
        for dance in content:
            if dance[0] == "s":
                amt = int(dance[1:])
                programs = programs[len(programs)-amt:] + programs[:len(programs)-amt]
            elif dance[0] == "x":
                pos1 = int(dance[1:dance.index("/")])
                pos2 = int(dance[dance.index("/")+1:])
                prog1 = programs[pos1]
                programs[pos1] = programs[pos2]
                programs[pos2] = prog1
            else:
                p1 = dance[1]
                p2 = dance[3]
                a, b = programs.index(p1), programs.index(p2)
                programs[b], programs[a] = programs[a], programs[b]
        orn = "".join(programs)
        if orn in orns:
            break
        else:
            orns.append(orn)
    return orns


def dance(orns,times):
    times = times % len(orns)
    return orns[times]

cycles = find_cycle(programs.copy())
answer_one = dance(cycles,1)
answer_two = dance(cycles,1000000000)

print("p1: " + answer_one)
print("p2: " + answer_two)
