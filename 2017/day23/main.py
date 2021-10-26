#Open file and compress contents into an array
from sympy import isprime
with open("input.txt") as f:
    content = f.read().split("\n")
    content = content[:len(content)-1]

ops = {
"set":"=",
"sub":"-=",
"mul":"*=",
}
def coprocess(reg_a_val):
    dex = 0
    mul_num = 0
    exec("a = " + str(reg_a_val))
    if reg_a_val == 1:
        h_val = 0
        for m in range(108400, 125400 + 17, 17):
            if not isprime(m):
                h_val += 1
        return h_val
    while dex < len(content):
        cmd = content[dex][:3]
        var = content[dex][4:5]
        if var not in locals() and not var.isdigit():
            exec(var + " = 0")
        if cmd in ops:
            val = content[dex][6:]
            exec(var + ops[cmd] + val)
            if cmd == "mul":
                mul_num += 1
        elif cmd == "jnz" and eval(var + "!= 0"):
            val = content[dex][6:]
            dex += int(eval("val"))
            continue
        dex += 1
    return mul_num



answer_one = str(coprocess(0))
answer_two = str(coprocess(1))

print("p1: " + answer_one)
print("p2: " + answer_two)
