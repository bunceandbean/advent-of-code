with open("input.txt") as f:
    nums = list(map(int,f.read().split("\n")[:~0]))
answer_one = str(sum(nums[i]>nums[i-1] for i in range(1,len(nums))))
answer_two = str(sum(sum(nums[i-3:i])<sum(nums[i-2:i+1]) for i in range(3,len(nums)+1)))
print("p1: " + answer_one)
print("p2: " + answer_two)
