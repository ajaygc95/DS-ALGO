from sortedcontainers import SortedList

nums = SortedList()

nums.add((10,20))
nums.add((40,50))
nums.add((30,40))
nums.add((40,40))
nums.add((50,40))
nums.add((60,40))
nums.add((70,40))

# idx = nums.bisect_right((50,60))
# print(idx)

start = 0
end = len(nums)-1
idx = 0
while start <= end:
    mid = (start+end)//2

    if nums[mid][0] == 40:
        idx = mid
        break
    else:
        start = mid+1
    