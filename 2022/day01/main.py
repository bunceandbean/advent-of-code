with open("input.txt") as f:
    content = list(map(lambda x: list(map(int, x.split("\n"))), f.read().split("\n\n")[:~0]))

top_three = [0,0,0]
for elf in content:
    total = sum(elf)
    for j in range(len(top_three)):
        if total > top_three[j]:
            top_three[j] = total
            top_three = sorted(top_three)
            break

answer_one = top_three[~0]
answer_two = sum(top_three)
print("p1:", answer_one)
print("p2:", answer_two)
