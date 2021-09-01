answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
notReqField = "cid"

passportCount = 0
fieldCount = 0
for passportStrip in content:
    if passportStrip == '':
        if fieldCount == 7:
            passportCount += 1
        fieldCount = 0
        continue
    for field in fields:
        if field in passportStrip:
            fieldCount += 1

answer = passportCount
print(answer)
