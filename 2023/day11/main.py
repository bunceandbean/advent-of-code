from copy import deepcopy

with open("input.txt") as f:
    content = [list(x) for x in f.read().split("\n")[:~0]]
    gal_cords = []
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == "#":
                gal_cords.append([i,j])

def day11(gal_cords, factor):
    for i in range(len(content) - 1, -1, -1):
        if "#" not in content[i]:
            for r in range(len(gal_cords)):
                if gal_cords[r][0] > i:
                    gal_cords[r][0] += factor
    for j in range(len(content[0]) -1 , -1, -1):
        if "#" not in [x[j] for x in content]:
            for r in range(len(gal_cords)):
                if gal_cords[r][1] > j:
                    gal_cords[r][1] += factor
    total = 0
    for cord in gal_cords:
        for sec_cord in gal_cords:
            total += abs(sec_cord[0] - cord[0]) + abs(sec_cord[1] - cord[1])
    return total//2

print("p1:", day11(deepcopy(gal_cords), 1))
print("p2:", day11(deepcopy(gal_cords), 999999))
