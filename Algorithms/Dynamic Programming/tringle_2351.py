input = [  [2],
          [3,4],
         [6,5,7],
        [4,1,8,3]
]

dptable = [[]]*(len(input))

for i in range(len(input)):
    dptable[i] = [0]*(i + 1)



for row in range(len(input)):

    dptable[row][0] = dptable[row-1][0] + input[row][0]
    dptable[row][-1] = dptable[row-1][-1] + input[row][-1]

for row in range(2, len(input)):
    for col in range(1,row):

        dptable[row][col] = min(dptable[row-1][col-1], dptable[row-1][col]) + input[row][col]

print(dptable)
print(min(dptable[-1]))











# #creating a 2D matrix
# # row = length(lastgrid)
# # col = length(input)

# # dptable = [ [0 for cols in range(rows+1)] for rows in range(len(input))] 

# rows = len(input)

# dptable = []

# for row in range(rows):
#     dptable.append([0]*(row+1))

# #setting up base cases
# #filling up first and last node

# dptable[0][0] = input[0][0]

# for row in range(1, len(input)):

#     #left row
#     dptable[row][0] = dptable[row-1][0] + input[row][0]

#     #right row
#     # dptable[row][-1] = dptable[row-1][row-1] + input[row][-1]

#     dptable[row][row] = dptable[row-1][row-1] + input[row][row]

# for row in range(2, len(input)):
#     for col in range(1,row):
#         dptable[row][col] = min(dptable[row-1][col-1],dptable[row-1][col]) + input[row][col]

# print(min(dptable[-1]))











