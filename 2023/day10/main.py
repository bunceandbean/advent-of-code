from shapely.geometry import Polygon, Point

with open("input.txt") as f:
    file_text = f.read()
    content = list(map(list, file_text.split("\n")[:~0]))
    file_txt = file_text.replace("\n", "")
    s_cord = (int(file_txt.find("S") / len(content[0])), file_txt.find("S") % len(content[0]))

items = {
    '|': [('N','S'), ('N','S')],
    '-': [('E','W'), ('E','W')],
    'L':[('S','W'), ('E','N')],
    'J':[('S','E'), ('W','N')],
    '7':[('E','N'), ('S','W')],
    'F':[('W','N'), ('S','E')],
}

neighs = [(-1,0),(0,1),(1,0),(0,-1)]
dirs = ('N', 'E', 'S', 'W')
visited = [s_cord]

def get_neighbors(pt):
    neighbors = []
    for neigh in neighs:
        new_pt = (pt[0] + neigh[0], pt[1] + neigh[1])
        if new_pt[0] >= 0 and new_pt[1] >= 0 and new_pt[0] < len(content) and new_pt[1] < len(content[0]):
            neighbors.append(new_pt)
        else:
            neighbors.append(())
    return neighbors


def get_first(S):
    bors = get_neighbors(S)
    first = []
    for i in range(len(bors)):
        if not bors[i]:
            continue
        if (item:=content[bors[i][0]][bors[i][1]]) in items and dirs[i] in items[item][0]:
            first.append((bors[i], items[item][1][items[item][0].index(dirs[i])]))
    return first

def get_next(pair: tuple[tuple, str]):
    cord, dir = pair
    adder = neighs[dirs.index(dir)]
    next = (cord[0] + adder[0], cord[1] + adder[1])
    if next not in visited and (item:=content[next[0]][next[1]]) in items:
        return (next, items[item][1][items[item][0].index(dir)])
    
step = 0
queue = get_first(s_cord)
while queue:
    step += 1
    next_queue = []
    for pair in queue:
        visited.append(pair[0])
        next = get_next(pair)
        if next:
            next_queue.append(next)
    queue = next_queue

visited_new = visited[::2]
visited_new += visited[::-1][1::2]
poly = Polygon(visited_new)
in_loop = 0
for i in range(len(content)):
    for j in range(len(content[0])):
        if (i,j) not in visited_new and poly.contains(Point(i,j)):
            in_loop += 1

print("p1:", step)
print("p2:", in_loop)