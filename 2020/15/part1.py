answer = 0
#Open file and compress lines into an array
start_nums = [2,0,6,12,1,3]
nums = []

for i in range(2020):
    if i < len(start_nums):
        nums.append(start_nums[i])
        continue
    if nums[len(nums)-1] in nums[:len(nums)-1]:
        indices = [i for i, x in enumerate(nums) if x == nums[len(nums)-1]]
        diff = indices[len(indices)-1] - indices[len(indices)-2]
        nums.append(diff)
    else:
        nums.append(0)
answer = nums[len(nums)-1]
print(answer)
