with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]
deer = {}
for line in content:
    dname = line[:line.index(" ")]
    rate = int(line[line.index("fly")+4:line.index("km/s")-1])
    time = int(line[line.index("for")+4:line.index('seconds')-1])
    rest = int(line[line.index("rest")+9:line.index("seconds.")-1])
    deer[dname] = [rate,time,rest]

def deer_race(ticks, want_points):
    tracker = {}
    points = {}
    for d in deer:
        tracker[d] = 0
        points[d] = 0
    #####################
    for i in range(ticks):
        for d in deer:
            time = i % (deer[d][1] + deer[d][2])
            if time < deer[d][1]:
                tracker[d] += deer[d][0]
        lead = max(tracker.values())
        for d in tracker:
            if tracker[d] == lead:
                points[d] += 1
    if want_points:
        return max(points.values())
    else:
        return max(tracker.values())

answer_one = str(deer_race(2503, False))
answer_two = str(deer_race(2503, True))
print("p1: " + answer_one)
print("p2: " + answer_two)
