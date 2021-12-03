with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

binary = ""
least = ""
for i in range(len(content[0])):
    bins = [x[i] for x in content]
    if bins.count("1") > len(bins)//2:
        binary += "1"
        least += "0"
    else:
        binary += "0"
        least += '1'

oxygen = 0
co2 = 0
crit_o = content.copy()
crit_c = content.copy()
for i in range(len(content[0])):
    bins_o = [x[i] for x in crit_o]
    bins_c = [x[i] for x in crit_c]
    if bins_o.count("1") >= bins_o.count("0"):
        crit_o = [x for x in crit_o if x[i] == "1"]
    else:
        crit_o = [x for x in crit_o if x[i] == "0"]
    if bins_c.count("1") < bins_c.count("0"):
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
