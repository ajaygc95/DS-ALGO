nums = [-2,1,-3,4,-1,2,1,-5,4]

maxsum = 0
for i in range(len(nums)):
    currsum = 0
    for j in range(i,len(nums)):
        currsum  += nums[j]

        if currsum > maxsum:
            maxsum = currsum
        

print(maxsum)
        
