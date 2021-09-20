#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = str(content[0])

def search(index):
    count = 0
    j = index
    while True:
        if content[j] == "!":
            j += 1
        elif content[j] == ">":
            return [j,count]
        else:
            count += 1
        j += 1

def clean(content):
    count = 0
    new_content = ""
    end = -1
    for i in range(len(content)):
        if not(i <= end):
            if content[i] == "<":
                search_return = search(i+1)
                end = search_return[0]
                count += search_return[1]
            else:
                new_content += content[i]
    return [new_content,count]


clean_return = clean(content)
clean_content = clean_return[0]
bracket_store = []
score = 0
for bracket in clean_content:
    if bracket == "{":
        bracket_store.append(bracket)
    elif bracket == "}":
        score += len(bracket_store)
        bracket_store.pop(len(bracket_store)-1)

answer_one = str(score)
answer_two = str(clean_return[1])
print("p1: " + answer_one)
print("p2: " + answer_two)
