with open("input.txt") as f:
    content = f.read()[:~0]

alpha = "abcdefghijklmnopqrstuvwxyz"

def react(content):
    while True:
        old = len(content)
        for ch in alpha:
            content = content.replace(f"{ch}{ch.upper()}", "")
            content = content.replace(f"{ch.upper()}{ch}", "")
        if old == len(content):
            break
    return len(content)

shortest = -1
for ch in alpha:
    test_content = content.replace(f"{ch}", "")
    test_content = test_content.replace(f"{ch.upper()}", "")
    reaction = react(test_content)
    if reaction < shortest or shortest == -1:
        shortest = reaction
    

print("p1:", react(content))
print("p1:", shortest)



