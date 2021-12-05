with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def lines(zeroes):
    pts = set()
    cross = set()
    for line in content:
        one = eval("(" + line[:line.index(" ")] + ")")
        two = eval("(" + line[line.index(">")+2:] + ")")
        delta = (two[0]-one[0], two[1]-one[1])
        if 0 in delta or zeroes:
            if 0 in delta:
                irange = range(one[0],two[0]+1) if delta[0] > 0 else range(two[0],one[0]+1)
                jrange = range(one[1],two[1]+1) if delta[1] > 0 else range(two[1],one[1]+1)
                for i in irange:
                    for j in jrange:
                        leng = len(pts)
                        pts.add((i,j))
                        if leng == len(pts):
                            cross.add((i,j))
            else:
                slope = delta[1]//delta[0]
                for i in range(abs(delta[0])+1):
                    leng = len(pts)
                    pt = (two[0]+i,two[1]+slope*i) if delta[0] < 0 else (one[0]+i,one[1]+slope*i)
                    pts.add(pt)
                    if leng == len(pts):
                        cross.add(pt)


    return len(cross)

answer_one = str(lines(False))
answer_two = str(lines(True))
print("p1: " + answer_one)
print("p2: " + answer_two)
