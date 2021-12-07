with open("input.txt") as f:
    content = [1 if x == "(" else -1 for x in f.read().strip()]
answer_one = str(sum(content))
answer_two = str([x+1 for x in range(len(content)) if sum(content[:x+1]) < 0][0])
print("p1: " + answer_one)
print("p2: " + answer_two)
