answer = 0
# Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def fill(content):
    seats = []
    for rowNum in range(len(content)):
        row = []
        for seatNum in range(len(content[rowNum])):
            if content[rowNum][seatNum] == "L":
                row.append("#")
            else:
                row.append(".")
        seats.append(row)
    return seats

seats = fill(content)

seatLayouts = []
def seatingSystem(seats):
    for rowNum in range(len(seats)):
        row = []
        for seatNum in range(len(seats[rowNum])):
            adjacent = []
            try:
                adjacent.extend([seats[rowNum-1][seatNum])
            if seats[rowNum][seatNum] == "L":
