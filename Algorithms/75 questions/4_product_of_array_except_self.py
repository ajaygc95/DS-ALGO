nums =[-1,1,0,-3,3]

prefix = [1]*len(nums)
prev_sum = 1
postfix = [1]* len(nums)

for i in range(1, len(nums)):
    prefix[i] = prev_sum
    prev_sum = nums[i]*prev_sum

prev_sum = 1
for i in range(len(nums)-1, -1, -1):
    postfix[i] = prev_sum
    prev_sum = nums[i]*prev_sum

result = []

for i in range(len(nums)):
    result.append(postfix[i]*prefix[i])

print(result)