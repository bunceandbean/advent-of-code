from collections import defaultdict
with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

dirs = defaultdict(int)
dir_queue = []
for line in content:
    if "$ cd" in line and ".." not in line:
        dir = line[line.index('cd') + 3 :]
        dir_queue.append("".join(dir_queue) + dir)
    elif "$ cd .." in line:
        dir_queue.pop()
    elif line[0].isdigit():
        for dir in dir_queue:
            dirs[dir] += int(line[:line.index(" ")])

unused_space = 30000000 - (70000000 - dirs["/"])
answer_one = sum(dirs[dir] for dir in dirs if dirs[dir] <= 100000)
answer_two = min(dirs[dir] for dir in dirs if unused_space <= dirs[dir])
print("p1:", answer_one)
print("p2:", answer_two)
