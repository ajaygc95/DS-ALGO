nums = [5,4,-1,7,8]

maxsum = nums[0]

currsum = 0
for i in range(len(nums)):

    if currsum < 0:
        currsum = 0
    currsum += nums[i]
    maxsum = max(maxsum, currsum)


        

print(maxsum)
        
