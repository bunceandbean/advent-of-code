def parse(file_name):
    try:
        with open(file_name) as f:
            return list(map(int,f.read().strip("\n").split(",")))
    except:
        return "Error"

def run(program):
    try:
        for i in range(len(program)//4):
            dex = i*4
            op = program[dex]
            num1, num2, mem = program[program[dex+1]], program[program[dex+2]], program[dex+3]
            if op == 1:
                program[mem] = num1 + num2
            elif op == 2:
                program[mem] = num1 * num2
            else:
                return program

    except:
        return "Error"
    return program
