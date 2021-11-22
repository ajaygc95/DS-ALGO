m = 8
n = 4

profit = [1,2,5,6]
weight = [2,3,4,5]


dptable = [[0]*(1+n) for _ in range(m+1)]


for i in range(len(dptable)):
    dptable[i][0] =0
    dptable[i][1] =1


for j in range(len(dptable[0])):
    dptable[0][j] = 0


for item in dptable:
    print(item)

