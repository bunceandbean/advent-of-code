import json
with open("input.txt") as f:
    cont_str = f.read()
    content = list(cont_str)

def count(content):
    chain = [0]
    total = 0
    for char in content:
        if char == "-" and len(chain) == 1:
            chain[0] = 1
        elif char.isdigit():
            chain.append(char)
        elif len(chain) > 1:
            flop = 1
            if chain[0]:
                flop = -1
            total += int("".join(chain[1:])) * flop
            chain = [0]
    return total
answer_one = str(count(content))

def no_red(input):
    def find_boundary(input, start, goal):
        val = 0
        idx = start
        while val != goal:
            idx -= goal
            if input[idx] == "}":
                val += -1
            if input[idx] == "{":
                val += 1
        return idx
    while True:
        pos = input.find(':"red"')
        if pos < 0:
            break
        start = find_boundary(input, pos, 1)
        end = find_boundary(input, pos, -1)
        input = input[:start] + "0" + input[end + 1:]
    return count(input)

answer_two = str(no_red(cont_str))
print("p1: " + answer_one)
print("p2: " + answer_two)
