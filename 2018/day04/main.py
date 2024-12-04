import re
with open("input.txt") as f:
    content = sorted(f.read().split("\n")[:~0])

guards = {}
cur_guard = -1
last_min = -1
last_state = ""
for line in content:
    mi = int(re.findall(":([0-6][0-9])", line)[0])
    date = line[1:11]
    if "begins shift" in line:
        guard_id = int(re.findall("#([0-9]*)",line)[0])
        if guard_id not in guards:
            guards[guard_id] = [0] * 60
        cur_guard = guard_id
        last_state = "up"
    elif "up" in line and last_state != "up":
        for i in range(last_min, mi):
            guards[cur_guard][i] += 1   
        last_state = "up"
    else:
        last_state = "asleep"
    last_min = mi

sleepy_guard = -1
sleep = -1
for guard in guards:
    total = sum(guards[guard])
    if total > sleep:
        sleepy_guard = guard
        sleep = total

best_min = guards[sleepy_guard].index(max(guards[sleepy_guard]))

most_sleepy_min = -1
sleepy_total = -1
min_guard = -1
for guard in guards:
    mins = guards[guard]
    for i in range(len(mins)):
        if mins[i] >= sleepy_total:
            sleepy_total = mins[i]
            most_sleepy_min = i
            min_guard = guard

print("p1:", best_min * sleepy_guard)
print("p2:", min_guard * most_sleepy_min)
