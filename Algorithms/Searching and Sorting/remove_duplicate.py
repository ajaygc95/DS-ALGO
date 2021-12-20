nums = [0,0,1,1,1,2,2,3,3,4]

i = 1
new_list = []

while i < len(nums)-1:
    if nums[i] != nums[i+1]:
        new_list.append(nums[i-1])
    i += 1
new_list.append(nums[i])

print(new_list)