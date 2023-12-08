def get_nums(strn):
    nums = []
    cur_num = ""
    for c in strn[::-1]:
        if c.isdigit():
            cur_num += c
        elif cur_num != "":
            nums.append(int(cur_num[::-1]))
            cur_num = ""
    nums.reverse()
    return nums

def day06(times, dists):
    run_mul = 1
    for i in range(len(times)):
        time = times[i]
        dist = dists[i]
        ways = 0
        for j in range(1, time):
            if (time - j) * (j) > dist:
                ways +=1 
        run_mul *= ways
    return run_mul


with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    times = get_nums(content[0])
    dists = get_nums(content[1])
    t = [int("".join(list(map(str,times))))]
    d = [int("".join(list(map(str,dists))))]

print("p1:", day06(times, dists))
print("p2:", day06(t, d))
