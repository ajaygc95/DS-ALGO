grid = [[0,0,0],[0,1,0],[0,0,0]]

dptable = [[0]*len(grid[0]) for _ in range(len(grid))]

dptable[0][0] = 1



for col in range(1,len(grid[0])):

    if grid[0][col] == 1:
        dptable[0][col] = 0
    
    else:
        dptable[0][col] = dptable[0][col-1]



for row in range(1, len(dptable)):
    if grid[row][0] == 1:
        dptable[row][0] = 0
    else:
        dptable[row][0] = dptable[row-1][0]


for row in range(1, len(dptable)):
    for col in range(1, len(dptable[0])):

        if grid[row][col] == 1:
            dptable[row][col] = 0

        else:
            dptable[row][col] = dptable[row-1][col] + dptable[row][col-1]

for item in dptable:
    print(item)