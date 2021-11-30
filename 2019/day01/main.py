with open("input.txt") as f:
    content = list(map(int,f.read().split("\n")[:~0]))

def fuel(num):
    return num//3 - 2
    
def fuel2(num):
    if fuel(num) > 0:
        return fuel(num) + fuel2(fuel(num))
    return 0

answer_one = str(sum(list(map(fuel,content))))
answer_two = str(sum(list(map(fuel2,content))))
print("p1: " + answer_one)
print("p2: " + answer_two)
