with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def checksum():
    two = 0
    three = 0
    for id in content:
        check2 = True
        check3 = True
        for ch in id:
            if id.count(ch) == 2 and check2:
                two += 1
                check2 = False
            elif id.count(ch) == 3 and check3:
                three += 1
                check3 = False
    return two * three

def correct():
    for id in content:
        for c_id in content[content.index(id):]:
            new_str = ""
            for ch1,ch2 in zip(id,c_id):
                if ch1 == ch2:
                    new_str += ch1
            if len(id) - len(new_str) == 1:
                return new_str

answer_one = str(checksum())
answer_two = correct()
print("p1: " + answer_one)
print("p2: " + answer_two)
