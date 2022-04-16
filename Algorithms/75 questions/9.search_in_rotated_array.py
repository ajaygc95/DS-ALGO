nums = [4,5,6,7,0,1,2]
target = 0
start = 0
end = len(nums)-1

while start <= end:

    mid = (start + end)//2

    if target < nums[mid] and target < nums[start]:
        start = mid+1
    else:
        end = mid-1

    
print(start)