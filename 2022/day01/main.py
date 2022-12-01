with open("input.txt") as f:
    content = sorted(list(map(lambda x: sum(map(int, x.split("\n"))), f.read().split("\n\n")[:~0])), reverse = True)

answer_one = content[0]
answer_two = sum(content[:3])
print("p1:", answer_one)
print("p2:", answer_two)
