nums = [-2,3,-4]

max_p = nums[0]

for i in range(len(nums)):
    total_cost = nums[i]
    for j in range(i+1, len(nums)):
        print(nums[i], nums[j], total_cost)
        total_cost = total_cost * nums[j]
        max_p = max(max_p,total_cost)

print(max_p)