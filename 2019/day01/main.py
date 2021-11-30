with open("input.txt") as f:
    content = list(map(int,f.read().split("\n")[:~0]))

def fuel(num):
    return num//3 - 2
def fuel2(num):
    sum = 0
    while fuel(num) > 0:
        num = fuel(num)
        sum += num
    return sum

answer_one = str(sum(list(map(fuel,content))))
answer_two = str(sum(list(map(fuel2,content))))
print("p1: " + answer_one)
print("p2: " + answer_two)
