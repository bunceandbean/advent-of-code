import hashlib
input = "ugkcyxxp"

def passcrack(input):
    password = ""
    suf = -1
    while len(password) < 8:
        suf += 1
        test = input + str(suf)
        result = hashlib.md5(test.encode()).hexdigest()
        while result[:5] != "00000":
            suf += 1
            test = input + str(suf)
            result = hashlib.md5(test.encode()).hexdigest()
        password += result[5:6]
    return password

def passcrackplus(input):
    password = ["","","","","","","",""]
    suf = -1
    while "" in password:
        suf += 1
        test = input + str(suf)
        result = hashlib.md5(test.encode()).hexdigest()
        valid = result[5:6].isdigit() and int(result[5:6]) <=7 and password[int(result[5:6])] == ""
        while result[:5] != "00000" or not valid:
            suf += 1
            test = input + str(suf)
            result = hashlib.md5(test.encode()).hexdigest()
            valid = result[5:6].isdigit() and int(result[5:6]) <=7 and password[int(result[5:6])] == ""
        password[int(result[5:6])] = result[6:7]
    return "".join(password)

answer_one = passcrack(input)
answer_two = passcrackplus(input)
print("p1: " + answer_one)
print("p2: " + answer_two)
