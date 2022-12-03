with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

run_sum_1 = 0
run_sum_2 = 0
for item in content:
    x,y = set(item[:len(item)//2]),set(item[len(item)//2:])
    ch = next(iter(x & y))
    run_sum_1 += chars.index(ch) + 1

for i in range(0,len(content),3):
    x,y,z = set(content[i]),set(content[i+1]),set(content[i+2])
    ch = next(iter(x & y & z))
    run_sum_2 += chars.index(ch) + 1

print("p1:", run_sum_1)
print("p2:", run_sum_2)
