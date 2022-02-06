

nums = [1,2,3]
target = 4

dptable = [0]*(target+1)
dptable[0] = 1

for i in range(1, target+1):

    for num in nums:
        if i - num >= 0:
            dptable[i] += dptable[i-num]


print(dptable[-1])
