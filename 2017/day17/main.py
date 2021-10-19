input = 303
def spinlock(times):
    buffer = [0]
    cur_index = 0
    for i in range(1,times+1):
        new_index = ((cur_index + input) % i) + 1
        buffer.insert(new_index,i)
        cur_index = new_index
    return buffer[cur_index +1]

def quicklock(times):
    loc = 0
    after_zero = 0
    for i in range(1,times+1):
        loc = (input+loc+1) % i
        if loc == 0:
            after_zero = i
    return after_zero

times_2017 = spinlock(2017)
zero_50mil = quicklock(50000000)
answer_one = str(times_2017)
answer_two = str(zero_50mil)
print("p1: " + answer_one)
print("p2: " + answer_two)
