with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    content = [x.replace(" ", "") for x in content]

def eval_math(exp, add_first):
    term = []
    nums = exp.replace("+","*").split("*")
    ops = [x for x in exp if x in "+*"]
    while len(ops) != 0:
        if add_first:
            while "+" in ops:
                nums[ops.index("+")] = str(eval(nums[ops.index("+")] + ops[ops.index("+")] + nums[ops.index("+") + 1]))
                nums.pop(ops.index("+") + 1)
                ops.pop(ops.index("+"))
            if len(ops) == 0:
                break
        nums[0] = str(eval(nums[0] + ops[0] + nums[1]))
        nums.pop(1)
        ops.pop(0)
    return int(nums[0])

def find_sum(content, add_first):
    total = 0
    for line in content:
        while True:
            if "(" in line:
                end = line.index(")")
                start = end
                while line[start] != "(":
                    start -= 1
                start += 1
                val = eval_math(line[start:end], add_first)
                line = line[:start-1] + str(val) + line[end+1:]
            else:
                total += eval_math(line, add_first)
                break
    return total

answer_one = find_sum(content, False)
answer_two = find_sum(content, True)
print("p1:", answer_one)
print("p2:", answer_two)
