points = {(1,1):20151125}
prev = 20151125
for i in range(2,3029+2947):
    for j in range(1,i+1):
        points[(i,j)] = (prev * 252533) % 33554393
        prev = points[(i,j)]
        i -= 1

answer_one = points[(2947,3029)]
print("p1:",answer_one)
print("Merry Christmas!")
