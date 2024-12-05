input = "246540-787419"

total = 0
total_only = 0
for i in range(int(input[:input.index("-")]), int(input[input.index("-")+1:]) + 1):
    if not (sorted(str(i)) == list(str(i))):
        continue
    total += any([x in str(i) for x in ["00","11","22","33","44","55","66","77","88","99"]])
    total_only += any([x in str(i) and x + x[0] not in str(i) for x in ["00","11","22","33","44","55","66","77","88","99"]])

print("p1:", total)
print("p2:", total_only)
