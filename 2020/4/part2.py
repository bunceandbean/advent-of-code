answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
notReqField = "cid" #why is this even a part of the puzzle...

def fieldReq(field,strip):
    if field == "byr":
        if int(strip) >= 1920 and int(strip) <= 2002:
            return True
    if field == "iyr":
        if int(strip) >= 2010 and int(strip) <= 2020:
            return True
    if field == "eyr":
        if int(strip) >= 2020 and int(strip) <= 2030 and len(strip) == 4:
            return True
    if field == "hgt":
        if "in" in strip:
            if int(strip[:strip.index("in")]) >= 59 and int(strip[:strip.index("in")]) <= 76:
                return True
        if "cm" in strip:
            if int(strip[:strip.index("cm")]) >= 150 and int(strip[:strip.index("cm")]) <= 193:
                return True
    if field == "hcl":
        hclChars = "ghijklmnopqrstuvwxyz"
        hclStrip = strip[1:]
        if len(hclStrip) == 6:
            checkIn = 0
            for val in hclStrip:
                if val in hclChars:
                    checkIn += 1
            if checkIn == 0:
                return True
    if field == "ecl":
        eclReqs = ["amb","blu","brn","gry","grn","hzl","oth"]
        for req in eclReqs:
            if req == strip:
                return True
    if field == "pid":
        if len(strip) == 9:
            return True
    return False


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
            strip = passportStrip[passportStrip.index(field) + 4:]
            if " " in strip:
                strip = strip[:strip.index(" ")]
            if fieldReq(field,strip):
                fieldCount += 1


answer = passportCount

print(answer)
