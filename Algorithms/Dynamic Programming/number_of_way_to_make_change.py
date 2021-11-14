
input = [1,2,3]
amount  = 3

dptable= [0]*(amount+1)
dptable[0] = 1

for i in range(1, len(dptable)):

    for coin in input:
        if coin >=0:
            dptable[i] = dptable[i-coin] + dptable[i]

print(dptable[-1])

