with open("input.txt") as f:
    content = [[*map(int,x.split("x"))] for x in f.read().split("\n")[:~0]]

prods = [[a[x%3]*a[x-1] for x in range(1,len(a)+1)] for a in content]
answer_one = str(sum([2*sum(x)+min(x) for x in prods]))
answer_two = str(sum([x[0]*x[1]*x[2] + 2*(sum(x)-max(x)) for x in content]))
print("p1: " + answer_one)
print("p2: " + answer_two)
