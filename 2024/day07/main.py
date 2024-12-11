with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    tests = [[int((y:=x.split(": "))[0]), [*map(int, y[1].split(" "))]] for x in content]

def new_total(op, total, num):
    match op:
        case '*':
            return total * num
        case '+':
            return total + num
        case '':
            return int(str(total) + str(num))
    return total

def dfs(ops, nums, total, i, target):
    if i > len(nums) - 1 or total > target:
        return total == target
    return any(dfs(ops, nums, new_total(ops[b], total, nums[i]), i+1, target) for b in range(len(ops)))

work_p1 = 0
work_p2 = 0
for test in tests:
    val,nums = test
    work_p1 += dfs(('*', '+'), nums, nums[0], 1, val) * val
    work_p2 += dfs(('*', '+', ''), nums, nums[0], 1, val) * val
            

print("p1:", work_p1)
print("p2:", work_p2)