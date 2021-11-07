n=7
steps=[2, 3]

dptable = [0] *(n+1)

dptable[0]  = 0
dptable[1] = 1

for i in range(2, n+1):


    a = dptable[i-steps[0]]

    b = dptable[i-steps[1]]

    if a <= 0:
        a = 0
        
    if b <= 0:
        b = 0

    dptable[i] = a + b

    # dptable[i] = dptable[i-1] + dptable[i-2]
print(dptable)
print(dptable[n])