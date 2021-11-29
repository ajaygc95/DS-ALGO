input = [[7,1],[2,2],[2,5],[5,1]]



dptable = [[0]*2 for _ in  range(len(input))]

dptable[0][1] = input[0][1]
dptable[0][0] = input[0][0]

dptable[1][1] = dptable[1-1][1] + input[1][1]
dptable[1][0] = dptable[1-1][0] + input[1][0]



for row in range(2,len(dptable)):

    for col in range(len(dptable[0])):
        if col == 0:
            dptable[row][col] = max(dptable[row-1][0] + input[row][0], dptable[row-2][1]+input[row][col],dptable[row][col])
        if col == 1:
            dptable[row][col] = max(dptable[row-1][1] + input[row][1], dptable[row-2][0]+input[row][col],dptable[row][col])


last_p = None

if dptable[-1][0] > dptable[-1][1]:
    last_p = 0
else: last_p  = 1

days = len(dptable)-1
result = []
while True:
    result.append(input[days][last_p])

    if days == 0:
        break


    if dptable[days][last_p] == dptable[days-1][last_p] + input[days][last_p]:
        days -= 1
    else:
        days -= 2
        if last_p == 0:
            last_p = 1
        else:
            last_p = 0


print(result)