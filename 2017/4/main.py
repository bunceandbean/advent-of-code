#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

total_one = 0
total_two = 0
for passphrase in content:
    words_one = []
    words_two = []
    word = ""
    word_total = []
    good_one = True
    good_two = True
    for i in range(len(passphrase)):
        if passphrase[i] != " ":
            word += passphrase[i]
            word_total.append(ord(passphrase[i]))
            word_total.sort()
        if passphrase[i] == " " or i == len(passphrase)-1:
            if word not in words_one:
                words_one.append(word)
                word = ""
            else:
                good_one = False
            if word_total not in words_two:
                words_two.append(word_total)
                word_total = []
            else:
                good_two = False
    if good_one:
        total_one += 1
    if good_two:
        total_two += 1
answer_one = total_one
answer_two = total_two
print("p1: " + str(answer_one))
print("p2: " + str(answer_two))
