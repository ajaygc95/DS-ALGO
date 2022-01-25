grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]]

dptable = [[0]*len(grid[0]) for _ in range(len(grid))]

dptable[0][0] = grid[0][0]

for col in range(1, len(grid[0])):
    dptable[0][col] = dptable[0][col-1] + grid[0][col]

for row in range(1, len(grid)):
    dptable[row][0] = dptable[row-1][0] + grid[row][0]


for row in range(1, len(grid)):
    for col in range(1, len(grid[0])):

        dptable[row][col] = min( dptable[row-1][col] + grid[row][col], dptable[row][col-1]+grid[row][col])

for item in dptable:
    print(item)


print(dptable[-1][-1])