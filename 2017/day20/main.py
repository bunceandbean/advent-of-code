#Open file and compress contents into an array
import copy
particles = []
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]
    i = 0
    for part in content:
        particles.append([])
        particles[i].append([int(x) for x in part[3:part.index("v")-3].split(",")])
        particles[i].append([int(x) for x in part[part.index("v")+3:part.index("a")-3].split(",")])
        particles[i].append([int(x) for x in part[part.index("a")+3:len(part)-1].split(",")])
        i += 1
manhat_p = copy.deepcopy(particles)
manhat = []
for l in range(len(manhat_p)):
    for i in range(1000):
        for j in range(len(manhat_p[l][2])):
            manhat_p[l][1][j] += manhat_p[l][2][j]
            manhat_p[l][0][j] += manhat_p[l][1][j]
    manhat.append(sum(abs(x) for x in manhat_p[l][0]))

for i in range(1000):
    #Check collisions
    cols = []
    for m in range(len(particles)):
        for b in range(m+1,len(particles)):
            if particles[m][0] == particles[b][0]:
                if b not in cols:
                    cols.append(b)
                if m not in cols:
                    cols.append(m)
    cols.sort(reverse=True)
    for dex in cols:
        particles.pop(dex)

    for j in range(len(particles)):
        for k in range(len(particles[j][2])):
            particles[j][1][k] += particles[j][2][k]
            particles[j][0][k] += particles[j][1][k]


answer_one = str(manhat.index(min(manhat)))
answer_two = str(len(particles))

print("p1: " + answer_one)
print("p2: " + answer_two)
