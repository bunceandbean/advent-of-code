with open("input.txt") as f:
    content = [*map(int,f.read().split("\n")[:~0])]

for num in content:
    for deltaNum in content:
        if num + deltaNum == 2020:
            answer_one = str(num*deltaNum)
for num in content:
    for deltaNum in content:
        if num + deltaNum < 2020:
            for omegaNum in content:
                if num + deltaNum + omegaNum == 2020:
                    answer_two = str(num*deltaNum*omegaNum)
print("p1: " + answer_one)
print("p2: " + answer_two)
