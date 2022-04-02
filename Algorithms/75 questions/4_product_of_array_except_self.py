nums =[-1,1,0,-3,3]

result = [1]* len(nums)
prev_sum = 1

for i in range(len(nums)):
    result[i] = prev_sum
    prev_sum = prev_sum*nums[i]

prev_sum = 1
for  j in range(len(nums)-1,-1, -1):
    result[j] = result[j]*prev_sum
    prev_sum = prev_sum*nums[j]

print(result)
# prefix = [1]*len(nums)
# prev_sum = 1
# postfix = [1]* len(nums)



# for i in range(len(nums)):
#     prefix[i] = prev_sum
#     prev_sum = nums[i]*prev_sum
# print(prefix)
# prev_sum = 1
# for i in range(len(nums)-1, -1, -1):
#     postfix[i] = prev_sum
#     prev_sum = nums[i]*prev_sum
# print(postfix)
# result = []

# for i in range(len(nums)):
#     result.append(postfix[i]*prefix[i])

