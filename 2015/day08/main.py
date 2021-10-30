with open("input.txt") as f:
    content = f.readlines()

code = 0
char = 0
sec_code = 0
for line in content:
    code += len(line)-1
    char += len(eval(line))
    sec_code += line.count("\\") + line.count('"') + 2


answer_one = str(code - char)
answer_two = str(sec_code)
print("p1: " + answer_one)
print("p2: " + answer_two)
