from itertools import chain
from functools import reduce
from operator import xor
#Open file and compress lines into an array
with open("input.txt") as f:
    content = f.read()
string_content = content.strip()
content = [int(n) for n in content.split(',')]
gen_256 = [x for x in range(256)]
def hash(content,gen_list,rounds):
    pos = 0
    skip = 0
    for i in range(rounds):
        for length in content:
            if pos + length > len(gen_list):
                sub = gen_list[pos:] + gen_list[:pos + length - len(gen_list)]
                sub.reverse()
                gen_list[pos:] = sub[:len(gen_list[pos:])]
                gen_list[:pos + length - len(gen_list)] = sub[len(gen_list[pos:]):]
            else:
                sub = gen_list[pos:pos+length]
                sub.reverse()
                gen_list[pos:pos+length] = sub
            pos = (pos + length + skip)%len(gen_list)
            skip += 1
    return [gen_list[0] * gen_list[1],gen_list]

ascii = [ord(x) for x in string_content] + [17,31,73,47,23]
sparse_hash = hash(ascii.copy(),gen_256.copy(),64)[1]
dense_hash = []
span = 0
while span < 256:
    dense_hash.append(reduce(xor,map(int,sparse_hash[span:span+16])))
    span += 16
hex_hash = "".join([hex(x)[2:].zfill(2) for x in dense_hash])

answer_one = str(hash(content.copy(),gen_256.copy(),1)[0])
answer_two = hex_hash
print("p1: " + answer_one)
print("p2: " + answer_two)
