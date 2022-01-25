
cost = [10,15,20]

dptable = [[] for _ in range(len(cost))]

dptable[0] = cost[0]
dptable[1] = cost[1]

for i in range(2, len(cost)):
    dptable[i] = min (dptable[i-1], dptable[i-2]) + cost[i]


print(min(dptable[-1], dptable[-2]))