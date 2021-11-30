with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    content = [eval('0'+x) for x in content]
def first_two():
    freqs = {0}
    freq = 0
    while True:
        for num in content:
            length = len(freqs)
            freq += num
            freqs.add(freq)
            if length == len(freqs):
                return freq

answer_one = str(sum(content))
answer_two = str(first_two())
print("p1: " + answer_one)
print("p2: " + answer_two)
