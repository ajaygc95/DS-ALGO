nums = [1,2,3,4,5,6,7,8,9]
target = 7
left = 0
right = len(nums)

while left < right:
    mid = (left+right)//2

    if nums[mid] < target:
        left = mid+1 
    else:
        right = mid


print(nums[left:right+1])


start = 0
end = len(nums)

while start+1 < end:
    mid = (start+end)//2

    if nums[mid] < target:
        start = mid
    else:
        end = mid

print(nums[start:end+1])