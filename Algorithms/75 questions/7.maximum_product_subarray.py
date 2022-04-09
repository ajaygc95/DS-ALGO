nums = [2, 3, -2, 4]

rest = nums[0]

currMin, currMax = 1, 1
for n in nums:

    currMax = max(n*currMax, n*currMin, n)
    currMin = min(n*currMax, n*currMin, n)

    rest = max(rest, currMax, currMin)

print(rest)