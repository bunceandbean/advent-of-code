#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
    content = [int(x[x.index("with") + 5:len(x)-1]) for x in content]

def gen_values(pair, times, multiple):
    matches = 0
    for i in range(times):
        pair[0] *= 16807
        pair[0] = pair[0] % 2147483647
        while multiple and pair[0] % 4 != 0:
            pair[0] *= 16807
            pair[0] = pair[0] % 2147483647
        pair[1] *= 48271
        pair[1] = pair[1] % 2147483647
        while multiple and pair[1] % 8 != 0:
            pair[1] *= 48271
            pair[1] = pair[1] % 2147483647
        if bin(pair[0])[-16:] == bin(pair[1])[-16:]:
            matches += 1
    return matches

answer_one = str(gen_values(content.copy(),40000000,False))
answer_two = str(gen_values(content.copy(),5000000, True))

print("p1: " + answer_one)
print("p2: " + answer_two)
