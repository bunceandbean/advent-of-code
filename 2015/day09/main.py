from collections import defaultdict
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]

opts = defaultdict(list)
dists = {}
for path in content:
    city1 = path[:path.index("to")-1]
    city2 = path[path.index("to")+3:path.index("=")-1]
    dist = int(path[path.index("=")+1:])
    dists[city1+city2] = dist
    opts[city1].append(city2)
    opts[city2].append(city1)

def find_dist(route):
    dist = 0
    route = list(route)
    for i in range(1,len(route)):
        for d in dists:
            if route[i] in d and route[i-1] in d:
                dist += dists[d]
                break
    return dist

def pathfinder(pos,past):
    poss = []
    if pos in past:
        return []
    past = past | {pos}
    if len(past) == len(opts):
        return [find_dist(past)]
    for route in opts[pos]:
        poss += pathfinder(route,past)
    return poss


# perm_cities = list(permutations(cities))
# min_dist = 1000
# max_dist = 0
# for perm in perm_cities:
#     pivot = perm[0]
#     total = 0
#     for next in perm[1:]:
#         for pos in opts[pivot]:
#             if pos[0] == next:
#                 total += pos[1]
#                 pivot = next
#                 break
#     if total < min_dist:
#         min_dist = total
#     if total > max_dist:
#         max_dist = total
print(pathfinder("Arbre",set()))
# answer_one = str(min_dist)
# answer_two = str(max_dist)
# print("p1: " + answer_one)
# print("p2: " + answer_two)
