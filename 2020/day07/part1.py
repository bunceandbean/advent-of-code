answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
count = 0
for rule in content:
    content[count] = rule.replace('.','')
    content[count] = [rule[:rule.index("bags") - 1],rule[rule.index("contain")+9:]]
    count += 1

validColors = []
def recursiveBag(color):
    for rule in content:
        if color in rule[1]:
            if rule[0] not in validColors:
                validColors.append(rule[0])
            recursiveBag(rule[0])

recursiveBag("shiny gold")
answer = len(validColors)
print(answer)
