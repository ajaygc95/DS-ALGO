input = [2, 3, 1, 0, 4, 7]

n = len(input)
good = n-1

print(input[n-1])

# for i in range(len(input)-2,-1,-1):

#     if input[i]+ i >= good:
#         good = i

# print(good)



dptable = [False]*(len(input)+1)

dptable[0] = True
dptable[1] = True

for i in range(1,len(dptable)):

    for item in range(1,input[i-1]+1):

        if i + item < len(dptable) and dptable[i]:

            if not dptable[i+item]:
                dptable[i+item] = True


print(dptable)