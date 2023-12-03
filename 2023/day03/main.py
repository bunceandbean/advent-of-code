with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    content = ["." + x + "." for x in content]
    content.append(len(content[0]) * ".")
    content.insert(0, len(content[0]) * ".")

adj = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]

num = ""
nums = []
idxs = []
syms = set()
gear_syms = []
gears = []
for x in range(len(content)):
    for y in range(len(content[0])):
        ch = content[x][y]
        if ch.isnumeric():
            num += ch
            continue
        if num != "":
            nums.append(int(num))
            idx = []
            for i in range(len(num)):
                idx.append((x,y-i-1))
            idxs.append(idx)
            num = ""
        if ch != ".":
            if ch == "*":
                gears.append((x,y))
                gear_syms.append(set())
            for a in adj:
                syms.add((x + a[0],y + a[1]))
                if ch == "*":
                    gear_syms[~0].add((x + a[0],y + a[1]))
                
sumd = 0
for i in range(len(nums)):
    for idx in idxs[i]:
        if idx in syms:
            sumd += nums[i]
            break

gear_sum = 0
for i in range(len(gears)):
    gear_nums = []
    for j in range(len(nums)):
        for idx in idxs[j]:
            if idx in gear_syms[i]:
                gear_nums.append(nums[j])
                break
    if len(gear_nums) == 2:
        gear_sum += gear_nums[0] * gear_nums[1]

            

print("p1:", sumd)
print("p2:", gear_sum)
