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
total = []
def recursiveValidBags(color):
    for rule in content:
        if color in rule[1]:
            if rule not in validColors:
                validColors.append(rule)
                total.append(sum(int(x) for x in rule[1] if x.isdigit()))
            recursiveValidBags(rule[0])


recursiveValidBags("shiny gold")

print(sum(total))
print(answer)
