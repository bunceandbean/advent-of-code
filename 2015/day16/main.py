with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]

sue = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

def find_aunt(outdated):
    for aunt in content:
        num = int(aunt[4:aunt.index(":")])
        arr = aunt[aunt.index(":")+1:].replace(" ","").split(",")
        valid = 0
        for val in arr:
            key = val[:val.index(":")]
            amt = int(val[val.index(":")+1:])
            if key in sue:
                if not outdated and amt == sue[key]:
                    valid += 1
                elif outdated and ((key == "cats" or key == "trees") and amt > sue[key]):
                    valid += 1
                elif outdated and ((key == "pomeranians" or key == "goldfish") and amt < sue[key]):
                    valid += 1
                elif outdated and amt == sue[key]:
                    valid += 1
            else:
                valid += 1
        if valid == len(arr):
            return num



answer_one = str(find_aunt(False))
answer_two = str(find_aunt(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
