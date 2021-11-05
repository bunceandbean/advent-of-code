from functools import reduce
input = 34000000

def sigma(num,times,check_num):
    thing = set(reduce(list.__add__,
                ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))
    r_t = []
    if check_num == 50:
        for item in list(thing):
            if num/item <= 50:
                r_t.append(item)
        return sum(r_t)*times
    return sum(thing)*times

def divisor_sum(init,times,cnum):
    house = init
    sig = sigma(house,times,cnum)
    while sig < input:
        house += 1
        sig = sigma(house,times,cnum)
    return house


answer_one = str(divisor_sum(100000,10,0))
answer_two = str(divisor_sum(100000,11,50))
print("p1: " + answer_one)
print("p2: " + answer_two)
