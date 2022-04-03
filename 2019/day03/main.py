with open("input.txt") as f:
    content = [x.split(",")for x in f.read().split("\n")[:~0]]

directs = {
    "U":[0,1],
    "D":[0,-1],
    "R":[1,0],
    "L":[-1,0]
}
def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    if rev:
        points.reverse()
    return points

def manhat(tup):
    return abs(tup[0]) + abs(tup[1])

def build_circuit(content, point, bool_point):
    wire_1 = set()
    wire_2 = set()
    total_steps = 0
    for wire in content:
        steps = 0
        last_pt = [0,0]
        for dir in wire:
            amt = int(dir[1:])
            unit = [directs[dir[0]][0]*amt, directs[dir[0]][1]*amt]
            new_pt = [last_pt[0] + unit[0], last_pt[1] + unit[1]]
            skip_first = True
            outer_break = False
            for pt in get_line(last_pt[0],last_pt[1],new_pt[0],new_pt[1]):
                if skip_first:
                    skip_first = False
                    continue
                steps += 1
                if bool_point and point == pt:
                    if wire == content[0]:
                        total_steps += steps
                        outer_break = True
                        break
                    else:
                        return total_steps + steps
                if wire == content[0]:
                    wire_1.add(pt)
                else:
                    wire_2.add(pt)
            last_pt = new_pt
            if outer_break:
                break
    closest_inter = min([manhat(x) for x in set(wire_1) & set(wire_2)])
    return [closest_inter, set(wire_1) & set(wire_2)]

answer = build_circuit(content, None, False)
answer_one = answer[0]

min_cross = -1
for pt in answer[1]:
    steps = build_circuit(content, pt, True)
    if steps < min_cross or min_cross < 0:
        min_cross = steps

answer_two = min_cross
print("p1:", answer_one)
print("p2:",answer_two)
