answer = 0
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

keypad = [[1,2,3],[4,5,6],[7,8,9]]
location = keypad[1][1]
row = 1
column = 1
code = []

for instruction in content:
    for go in instruction:
        if go == "U":
            if row > 0:
                row -= 1
        if go == "D":
            if row < 2:
                row += 1
        if go == "L":
            if column > 0:
                column -= 1
        if go == "R":
            if column < 2:
                column += 1
    location = keypad[row][column]
    code.append(location)

print(code)
