with open("input.txt") as f:
    content = f.read().split("\n")[:~0]

def bubble_solve(edges, nums):
    change = True
    while change:
        change = False
        for i in range(len(nums)-1):
            if nums[i] not in edges[nums[i+1]]:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
                change = True
    return nums[len(nums)//2]

edges = {}
for line in content[:content.index("")]:
    x,y = int(line[:line.index("|")]), int(line[line.index("|")+1:])
    if y in edges:
        edges[y].add(x)
    else:
        edges[y] = set([x])

total_p1 = 0
total_p2 = 0
for line in content[content.index("")+1:]:
    nums = [*map(int, line.split(","))]
    if all([(nums[i] in edges[nums[i+1]]) for i in range(len(nums)-1)]):
        total_p1 += nums[len(nums)//2] 
    else:
        total_p2 += bubble_solve(edges, nums)

print("p1:", total_p1)
print("p2:", total_p2)