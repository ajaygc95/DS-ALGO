
# Pascal Triangle

n = 5

dptable = [ [0]*(i+1) for i in range(n)]

dptable[0][0] = 1


for col in range(len(dptable)):
    dptable[col][0] = 1
    dptable[col][-1] = 1

for row in range(2, n):
    for col in range(1, row):
        dptable[row][col] = dptable[row-1][col-1] + dptable[row-1][col]

for item in dptable:
    print(item)
































# n=7

# dptable = [[0]*(i+1) for i in range(n)]


# dptable[0][0] = 1

# for i in range(n):
#     dptable[i][0] = 1
#     dptable[i][-1] = 1

# for row in range(2, n):
#     for col in range(1,row):
#         dptable[row][col] = dptable[row-1][col-1] + dptable[row-1][col]

# for item in dptable:
#     nn = n-len(item)
#     result =" "* nn
#     print(result,item)