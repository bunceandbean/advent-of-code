with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    seeds = list(map(int, content[0][content[0].index(":")+2:].split(" ")))
    ranges_1 = []
    ranges_2 = []
    for i in range(0, len(seeds), 2):
        ranges_1.append((seeds[i], seeds[i]))
        ranges_1.append((seeds[i+1], seeds[i+1]))
        ranges_2.append((seeds[i], seeds[i] + seeds[i+1] - 1))
    maps = []
    cur_dir = {}
    for line in content[3:]:
        if "to" in line:
            maps.append(cur_dir)
            cur_dir = {}
            continue
        if not line:
            continue
        nums = list(map(int, line.split(" ")))
        add = nums[2]
        cur_dir[(nums[1], nums[1] + add - 1)] = (nums[0], nums[0] + add -1)
    maps.append(cur_dir)

def day05(ranges):
    queue = ranges
    for table in maps:
        next_queue = []
        while queue:
            ran = queue.pop(0)
            raw = True
            for mapp in table:
                if mapp[1] < ran[0] or ran[1] < mapp[0]:
                    continue
                if ran[0] <= mapp[0] and mapp[1] <= ran[1]:
                    raw = False
                    next_queue.append((table[mapp][0], table[mapp][1]))
                    if ran[0] != mapp[0]:
                        queue.append((ran[0], mapp[0] - 1))
                    if ran[1] != mapp[1]:
                        queue.append((mapp[1] + 1, ran[1]))
                    break
                if mapp[0] < ran[0] and ran[1] < mapp[1]:
                    raw = False
                    next_queue.append((table[mapp][0] + (ran[0] - mapp[0]), table[mapp][0] + (ran[1] - mapp[0])))
                    break
                if mapp[0] <= ran[0] and mapp[1] <= ran[1]:
                    raw = False
                    next_queue.append((table[mapp][0] + (ran[0] - mapp[0]), table[mapp][1]))
                    if mapp[1] != ran[1]:
                        queue.append((mapp[1] + 1, ran[1]))
                    break
                if ran[0] <= mapp[0] and ran[1] <= mapp[1]:
                    raw = False
                    next_queue.append((table[mapp][0], table[mapp][0] + (ran[1] - mapp[0])))
                    if ran[0] != mapp[0]:
                        queue.append((ran[0], mapp[0] - 1))
                    break
            if raw:
                next_queue.append(ran)
        queue = next_queue
    return min(x[0] for x in queue)
            
                                      
print("p1:", day05(ranges_1))
print("p2:", day05(ranges_2))
