import random
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

coords = []

def variations(coord,inactive_check):
    vars = []
    list = [-1,0,1]
    total = 0
    to_26 = []
    if inactive_check:
        while(len(to_26) < 26):
            temp = [coord[0],coord[1],coord[2]]
            temp[0] = coord[0] + random.choice(list)
            temp[1] = coord[1] + random.choice(list)
            temp[2] = coord[2] + random.choice(list)
            if temp not in vars and temp != coord and temp not in coords:
                vars.append(temp)
            elif temp not in to_26 and temp != coord:
                to_26.append(temp)
    else:
        while(len(vars) < 26):
            temp = [coord[0],coord[1],coord[2]]
            temp[0] = coord[0] + random.choice(list)
            temp[1] = coord[1] + random.choice(list)
            temp[2] = coord[2] + random.choice(list)
            if temp not in vars and temp != coord:
                vars.append(temp)
    return vars

y_count = 0
for y in content:
    x_count = 0
    for x in y:
        if x == "#":
            coords.append([x_count,y_count,0])
        x_count += 1
    y_count += 1


for i in range(6):
    new_round = []
    #active check
    for coord in coords:
        active_list = 0
        for c in coords:
            if c is not coord and abs(c[0] - coord[0]) <= 1 and abs(c[1] - coord[1]) <= 1 and abs(c[2] - coord[2]) <= 1:
                active_list += 1
        if active_list == 3 or active_list == 2:
            new_round.append(coord)

    #inactive check

    coords = list(new_round)
    print(coords)

print(len(coords))
