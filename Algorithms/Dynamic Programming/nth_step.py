n=7
steps=[2, 3]

dptable = [0] *(n+1)

dptable[0]  = 0
dptable[1] = 1

for i in range(2, n+1):
    dptable[i] = dptable[i-steps[0]] + dptable[i-steps[1]]

    # dptable[i] = dptable[i-1] + dptable[i-2]
print(dptable)
print(dptable[n])