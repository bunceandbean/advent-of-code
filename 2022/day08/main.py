with open("input.txt") as f:
    content = [list(map(int,list(x))) for x in f.read().split("\n")[:~0]]

total = 0
max_score = 0
for i in range(len(content)):
    for j in range(len(content[0])):
        if i == 0 or j == 0 or i == len(content) -1 or j == len(content[0])-1:
            total += 1
            continue
        col = [content[x][j] for x in range(len(content))]
        dirs = (list(reversed(content[i][:j])), content[i][j+1:], list(reversed(col[:i])), col[i+1:])
        total += content[i][j] > min(map(lambda x: max(x), dirs))
        cum_score = 1
        for path in dirs:
            score = 1
            for t in range(len(path)):
                if path[t] < content[i][j]:
                    score += 1
                else:
                    break
                score -= t == len(path) -1
            cum_score *= score
        max_score = max(cum_score, max_score)

answer_one = total
answer_two = max_score
print("p1:", answer_one)
print("p2:", answer_two)
