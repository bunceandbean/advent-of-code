import re
with open("input.txt") as f:
    content = "do()" + f.read()[:~0] + "don't()"

def get_muls(text):
    return sum(int(x[0]) * int(x[1]) for x in re.findall("mul\(([0-9]+),([0-9]+)\)", text))

dos = re.findall("do\(\)([\S\s]*?)don't\(\)", content)

print("p1:", get_muls(content))
print("p2:", sum(get_muls(x) for x in dos))