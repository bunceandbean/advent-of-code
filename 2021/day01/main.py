with open("input.txt") as f:
    nums = list(map(int,f.read().split("\n")[:~0]))

sums = [sum(nums[i:i+3]) for i in range(len(nums))]
answer_one = str(len([i for i in range(1,len(nums)) if nums[i]>nums[i-1]]))
answer_two = str(len([i for i in range(1,len(sums)) if sums[i]>sums[i-1]]))
print("p1: " + answer_one)
print("p2: " + answer_two)
