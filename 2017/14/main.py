from itertools import chain
from functools import reduce
from operator import xor
input = "vbqugkhl"
def hash(content,rounds):
    gen_list = [x for x in range(256)]
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
    sparse_hash = gen_list
    dense_hash = []
    span = 0
    while span < 256:
        dense_hash.append(reduce(xor,map(int,sparse_hash[span:span+16])))
        span += 16
    return "".join([hex(x)[2:].zfill(2) for x in dense_hash])

def count_squares(input):
    squares = 0
    for i in range(128):
        concat = input + "-" + str(i)
        ascii = [ord(x) for x in concat] + [17,31,73,47,23]
        h = hash(ascii,64)
        binary = bin(int('1'+h, 16))[3:]
        squares += binary.count("1")
    return squares

def count_regions(input):
    grid = []
    for i in range(128):
        concat = input + "-" + str(i)
        ascii = [ord(x) for x in concat] + [17,31,73,47,23]
        h = hash(ascii,64)
        binary = bin(int('1'+h, 16))[3:]
        grid.append(list(binary))
    points = []
    regions = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                points.append([i,j])
    for point in points:
        region = [point]
        for point in region:
            vars = [[point[0]-1,point[1]],[point[0]+1,point[1]],[point[0],point[1]+1],[point[0],point[1]-1]]
            for var in vars:
                if var in points and var not in region:
                    region.append(points.pop(points.index(var)))
        regions += 1
    return regions


answer_one = str(count_squares(input))
answer_two = str(count_regions(input))
print("p1: " + answer_one)
print("p2: " + answer_two)
