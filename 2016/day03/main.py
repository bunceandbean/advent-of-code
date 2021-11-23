answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip().split(' ') for x in content]

for i in range(len(content)):
    while '' in content[i]:
        content[i].remove('')
    content[i] = [int(x) for x in content[i]]

def check_tri(content):
    valid = 0
    for t in content:
        if t[0] + t[1] > t[2] and t[2] + t[1] > t[0] and t[0] + t[2] > t[1]:
            valid += 1
    return valid

col = []
for i in range(3):
    for j in range(len(content)//3):
        tri = []
        for k in range(3):
            tri.append(content[j*3+k][i])
        col.append(tri)

answer_one = str(check_tri(content))
answer_two = str(check_tri(col))
print("p1: " + answer_one)
print("p2: " + answer_two)
