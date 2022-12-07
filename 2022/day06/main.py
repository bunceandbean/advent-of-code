with open("input.txt") as f:
    content = f.read()

def find_marker(char_length):
    for i in range(len(content)):
        nums = set(content[i:i+char_length])
        if len(nums) == char_length:
            return i + char_length

print("p1:", find_marker(4))
print("p2:", find_marker(14))
