answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

valid = 0
for triangle in content:
    one = ""
    two = ""
    three = ""
    whereAmI = 1
    count = 0
    for char in triangle:
        if char.isdigit():
            if whereAmI == 1:
                one = one + char
                if triangle[count + 1] == " ":
                    whereAmI = 2
            elif whereAmI == 2:
                two = two + char
                if triangle[count+1] == " ":
                    whereAmI = 3
            elif whereAmI == 3:
                three = three + char
                if count == len(triangle) - 1:
                    break
        count += 1

    one = int(one)
    two = int(two)
    three = int(three)
    if one + two > three and three + two > one and one + three > two:
        valid += 1

answer = valid
print(answer)
