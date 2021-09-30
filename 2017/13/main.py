#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]
    content = [[int(x[:x.index(":")]),int(x[x.index(":") + 2:])] for x in content]

firewall = []
for i in range(content[len(content)-1][0]+1):
    added = False
    for arr in content:
        if arr[0] == i:
            firewall.append(arr[1])
            added = True
            break
    if not added:
        firewall.append(1)

threat = 0
detected = True
pico_delay = -1
while detected:
    pico_delay += 1
    detected = False
    for i in range(len(firewall)):
        if firewall[i] != 1 and (pico_delay+i) % (2*(firewall[i]-1)) == 0:
            detected = True
            if pico_delay == 0:
                threat += firewall[i]*i
            else:
                break

answer_one = str(threat)
answer_two = str(pico_delay)
print("p1: " + answer_one)
print("p2: " + answer_two)
