###################################
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'intcode')))
###################################
import intcode
content = intcode.parse("input.txt")
content[1] = 12
content[2] = 2

a1_out = intcode.run(content.copy())[0]
a2_out = 0

for noun in range(100):
    for verb in range(100):
        content[1] = noun
        content[2] = verb
        if intcode.run(content.copy())[0] == 19690720:
            a2_out = 100 * noun + verb

answer_one = str(a1_out)
answer_two = str(a2_out)
print("p1: " + answer_one)
print("p2: " + answer_two)
