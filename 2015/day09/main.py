from itertools import permutations
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]

cities = []
opts = {}
for path in content:
    city1 = path[:path.index("to")-1][0:2]
    city2 = path[path.index("to")+3:path.index("=")-1][0:2]
    dist = int(path[path.index("=")+1:])
    if city1 not in cities:
        cities.append(city1)
        opts[city1] = []
    if city2 not in cities:
        cities.append(city2)
        opts[city2] = []
    opts[city1].append([city2,dist])
    opts[city2].append([city1,dist])

perm_cities = list(permutations(cities))
min_dist = 1000
max_dist = 0
for perm in perm_cities:
    pivot = perm[0]
    total = 0
    for next in perm[1:]:
        for pos in opts[pivot]:
            if pos[0] == next:
                total += pos[1]
                pivot = next
                break
    if total < min_dist:
        min_dist = total
    if total > max_dist:
        max_dist = total

answer_one = str(min_dist)
answer_two = str(max_dist)
print("p1: " + answer_one)
print("p2: " + answer_two)
