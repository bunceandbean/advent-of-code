with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

binary = ""
least = ""
for i in range(len(content[0])):
    bins = [int(x[i]) for x in content]
    binary += str(int(sum(bins) > len(bins)//2))
    least += str(int(not (sum(bins) > len(bins)//2)))

oxygen = 0
co2 = 0
crit_o = crit_c = content.copy()
for i in range(len(content[0])):
    bins_o = [x[i] for x in crit_o]
    bins_c = [x[i] for x in crit_c]
    if sum(map(int,bins_o)) >= len(bins_o)/2:
        crit_o = [x for x in crit_o if x[i] == "1"]
    else:
        crit_o = [x for x in crit_o if x[i] == "0"]
    if sum(map(int,bins_c)) < len(bins_c)/2:
        crit_c = [x for x in crit_c if x[i] == "1"]
    else:
        crit_c = [x for x in crit_c if x[i] == "0"]
    if len(crit_o) == 1:
        oxygen = int(crit_o[0],2)
    if len(crit_c) == 1:
        co2 = int(crit_c[0],2)

answer_one = str(int(binary,2)*int(least,2))
answer_two = str(co2*oxygen)
print("p1: " + answer_one)
print("p2: " + answer_two)
