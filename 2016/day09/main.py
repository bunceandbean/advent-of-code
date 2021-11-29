with open("input.txt") as f:
    content = f.read().split("\n")[:~0][0]

def decompress(content, recursive):
    total = 0
    i = 0
    if not recursive:
        while i < len(content):
            if content[i] == "(":
                scope = content[i:]
                length = int(scope[scope.index("(")+1:scope.index("x")])
                rep = int(scope[scope.index("x")+1:scope.index(")")])
                total += length*rep
                i += scope.index(")") + length
            i += 1
    else:
        weights = [1]*len(content)
        i = 0
        while i < len(content):
            if content[i] == "(":
                scope = content[i:]
                length = int(scope[scope.index("(")+1:scope.index("x")])
                rep = int(scope[scope.index("x")+1:scope.index(")")])
                for j in range(i+scope.index(")")+1,i+scope.index(")")+1+length):
                    weights[j] *= rep
                i += scope.index(")")+1
            else:
                total += weights[i]
                i += 1
    return total

answer_one = str(decompress(content, False))
answer_two = str(decompress(content, True))
print("p1: " + answer_one)
print("p2: " + answer_two)
