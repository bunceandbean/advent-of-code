with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def bubble_solve(edges, nums):
    change = True
    ordered = True
    while change:
        change = False
        for i in range(len(nums)-1):
            if nums[i] not in edges[nums[i+1]]:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
                change = True
                ordered = False
    return (nums[len(nums)//2], ordered) 

edges = {}
for line in content[:content.index("")]:
    x,y = int(line[:line.index("|")]), int(line[line.index("|")+1:])
    if y in edges:
        edges[y].add(x)
    else:
        edges[y] = set([x])
        
totals = [0,0]
for line in content[content.index("")+1:]:
    nums = [*map(int, line.split(","))]
    mid, ordered = bubble_solve(edges, nums)
    totals[not ordered] += mid

print("p1:", totals[0])
print("p2:", totals[1])