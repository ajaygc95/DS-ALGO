input = [1,2,3]
amount  = 3


dptable= [0]*(amount+1)

count = 0

for i in range(1,len(dptable)):


    for coin in input:
        if i - coin >= 0:

            if i -coin == 0:
                dptable[i] = dptable[i-1] + 1



print(dptable[i])