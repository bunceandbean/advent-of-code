with open('input.txt') as f:
    content = f.read().strip("/n")

def turing(times):
    tape = [0]
    pos = 0
    states = [[[1,1,1],[0,-1,1]],[[0,1,2],[1,-1,1]],[[1,1,3],[0,-1,0]],[[1,-1,4],[1,-1,5]],[[1,-1,0],[0,-1,3]],[[1,1,0],[1,-1,4]]]
    state = 0
    for i in range(times):
        write = states[state][tape[pos]][0]
        move = states[state][tape[pos]][1]
        new_state = states[state][tape[pos]][2]
        tape[pos] = write
        pos += move
        if pos < 0:
            tape.insert(0,0)
            pos = 0
        elif pos >= len(tape):
            tape.append(0)
        state = new_state
    return tape.count(1)


answer_one = str(turing(12586542))
answer_two = "Merry Christmas!"
print("p1: " + answer_one)
print(answer_two)
