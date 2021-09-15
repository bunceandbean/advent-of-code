#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
var_list ={}
max_num = 0
for line in content:
    var = line[:line.index(" ")]
    line = line[line.index(" ") + 1:]
    if var not in var_list:
        var_list[var] = 0
    delta = 1 if line[:line.index(" ")] == "inc" else -1
    num = int(line[line.index(" ") + 1:line.index("if")-1])
    delta = num * delta
    expression = line[line.index("if") + 3:]
    var_bool = expression[:expression.index(" ")]
    if var_bool not in var_list:
        var_list[var_bool] = 0
    expression = "var_list['" + var_bool + "']" + expression[expression.index(" "):]
    if eval(expression):
        var_list[var] += delta
        if var_list[var] >= max_num:
            max_num = var_list[var]

num_list = []
for var in var_list:
    num_list.append(var_list[var])
max_val = max(num_list)
answer_one = str(max_val)
answer_two = str(max_num)

print("p1: " + answer_one)
print("p2: " + answer_two)
