input = [[17,2,17], [16,16,5],[14,3,19]]


dptable = [[0]*3 for _ in range(len(input))]


for i in range(len(input)):

    dptable[0][i] = input[0][i]


for i in range(1, len(input)):

    dptable[i][0] = input[i][0] + min(dptable[i-1][1],dptable[i-1][2])
    dptable[i][1] = input[i][1] + min(dptable[i-1][0],dptable[i-1][2])
    dptable[i][2] = input[i][2] + min(dptable[i-1][0],dptable[i-1][1])

print(min(dptable[-1]))


