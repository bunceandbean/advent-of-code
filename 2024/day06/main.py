with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    map_dict = {'.':set(), '#': set()}
    pos = (0,0)
    for i in range(len(content)):
        for j in range(len(content)):
            if content[i][j] in ('.', '^'):
                map_dict['.'].add((i,j))
                pos = (i,j) if content[i][j] == '^' else pos
            else:
                map_dict['#'].add((i,j))

dir_map = {'^': (-1,0), '>': (0,1), '<': (0,-1), 'v':(1,0)}
order = ['^', '>', 'v', '<']

def run_map(pos):
    visited = set([pos])
    history = set((pos[0], pos[1], '^'))
    dir = '^'
    cycle = False
    while True:
        go = dir_map[dir]
        next = (go[0] + pos[0], go[1] + pos[1])
        if next in map_dict['.']:
            pos = next
        elif next in map_dict['#']:
            dir = order[(order.index(dir) + 1) % 4]
        else:
            break
        visited.add(pos)
        if (pos[0], pos[1], dir) in history:
            cycle = True
            break
        history.add((pos[0], pos[1], dir))
    return (visited, cycle)

p1_run = run_map(pos)
print("p1:", len(p1_run[0]))

count = 0
for tup in p1_run[0]:
    i,j = tup
    if content[i][j] == '.':
        map_dict['.'].remove((i,j))
        map_dict['#'].add((i,j))
        if run_map(pos)[1]:
            count += 1
        map_dict['.'].add((i,j))
        map_dict['#'].remove((i,j))

print("p2:", count)