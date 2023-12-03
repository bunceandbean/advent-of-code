with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

word_map = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

def decode(day2):
    if day2:
        for i in range(len(content)):
            for word in word_map:
                content[i] = content[i].replace(word, word[0] + word_map[word] + word[~0])
    sumd = 0
    for line in content:
        num = ""
        for ch in line:
            if ch.isdigit():
                num += ch
        sumd += int(num[0] + num[~0])
    return sumd

print("p1:", decode(False))
print("p2:", decode(True))