input = "cqjxjnds"

def pass_check(password):
    #straight check
    straight = False
    for i in range(len(password)-2):
        if ord(password[i+2]) - ord(password[i+1]) == 1 and ord(password[i+1]) - ord(password[i]) == 1:
            straight = True
    if not straight:
        return False
    #i,o,l check
    for char in password:
        if char == "i" or char == "o" or char == "l":
            return False
    #pairs check
    pairs = 0
    skip = False
    for i in range(len(password)-1):
        if skip:
            skip = False
            continue
        if password[i+1] == password[i]:
            pairs += 1
            skip = True
    if pairs < 2:
        return False
    return True

def gen_pass(input):
    first = True
    while not pass_check(input) or first:
        first = False
        list_in = list(input)
        curr = len(list_in) - 1
        list_in[curr] = chr((ord(list_in[curr]) + 1 - 97) % 26 + 97)
        while list_in[curr] == 'a':
            curr -= 1
            list_in[curr] = chr((ord(list_in[curr]) + 1 - 97) % 26 + 97)
        input = "".join(list_in)
    return input

answer_one = gen_pass(input)
answer_two = gen_pass(answer_one)
print("p1: " + answer_one)
print("p2: " + answer_two)
