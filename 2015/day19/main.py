with open("input.txt") as f:
    content = f.read().split("\n")
    mol = content[len(content)-2]
    content = content[:len(content)-3]

mole = []
skip = False
for i in range(len(mol)):
    if skip:
        skip = False
        continue
    if mol[i].isupper():
        if mol[(i+1)%len(mol)].islower():
            skip = True
            mole.append(mol[i] + mol[(i+1)%len(mol)])
            continue
        else:
            mole.append(mol[i])

pos = []
for i in range(len(mole)):
    for rule in content:
        if mole[i] == rule[:rule.index("=")-1]:
            old = mole[i]
            mole[i] = rule[rule.index(">")+2:]
            string = ''.join(mole)
            mole[i] = old
            if string not in pos:
                pos.append(string)

chem_eq = len(mole) - (mole.count("Rn") + mole.count("Ar")) - 2*mole.count("Y") -1

answer_one = str(len(pos))
answer_two = str(chem_eq)
print("p1: " + answer_one)
print("p2: " + answer_two)
