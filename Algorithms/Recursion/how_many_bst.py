n= 5
dptable = [0]*(n+1)

dptable[0] = 1
dptable[1] = 1 


for i in range(2,len(dptable)):

    for j in range(i):

        print(i,j)

        dptable[i] += dptable[j] * dptable[i-j-1]



print(dptable)