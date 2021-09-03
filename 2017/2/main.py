answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

num_content = []
for line in content:
    line_list = []
    num = ""
    for i in range(len(line)):
        if line[i] != "\t" and i != len(line)-1:
            num += line[i]
        else:
            if i == len(line)-1:
                num += line[i]
            line_list.append(int(num))
            num = ""
    num_content.append(line_list)

checksum = 0
for line in num_content:
    checksum += max(line)-min(line)

answer = checksum
print("p1: " + str(answer))
#######################################
div_sum = 0
for line in num_content:
    for i in range(len(line)):
        front = line[i:]
        for num in front:
            div_even = line[i] % num == 0 and line[i] > num or num % line[i] == 0 and num > line[i]
            if div_even:
                div_sum += line[i] // num + num // line[i]
answer = div_sum
print("p2: " + str(answer))
