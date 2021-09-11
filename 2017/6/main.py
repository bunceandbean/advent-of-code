#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.split() for x in content]
content = content[0]
for num in range(len(content)):
    content[num] = int(content[num])

def find_cycles(content):
    past_mem = []
    past_mem.append(content.copy())
    while True:
        max_num = max(content)
        max_index = content.index(max_num)
        content[max_index] = 0
        i = max_index + 1
        while max_num > 0:
            content[i % len(content)] += 1
            max_num -= 1
            i += 1
        if content.copy() in past_mem:
            break
        past_mem.append(content.copy())
    return [len(past_mem), content]

results = find_cycles(content)
answer_one = results[0]
answer_two = find_cycles(results[1])[0]
print("p1: " + str(answer_one))
print("p2: " + str(answer_two))
