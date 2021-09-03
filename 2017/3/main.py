import math
answer = 0
num = 347991
def find_distance(input):
    to_square = 1
    shell = 0
    while to_square * to_square < num:
        to_square += 2
        shell += 1
    to_square -= 2
    diff = num - to_square * to_square
    while diff - shell >= 0:
        diff -= shell
    return diff + shell

answer = find_distance(347991)

print("p1: " + str(answer))
#####################################
