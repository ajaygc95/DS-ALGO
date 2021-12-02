
n = 3
new_path = {1: [6, 8], 2: [7, 9], 3:[4, 8], 4: [3, 9, 0], 5: [],
             6: [0, 1, 7], 7: [6, 2], 8: [1, 3], 9: [2, 4], 0: [4, 6]}


dptable = [[0]*(len(new_path)) for _ in range(n) ]


for i in range(len(dptable[0])):
    dptable[0][i] = 1

# for item in dptable:
#     print(item)



for i in range(1,n):
    for j in range(10):
        
        for item in new_path[j]:
            dptable[i][j] += dptable[i-1][item]


print(dptable[-1][-1])

# dp = [1]* 10
# print(dp)


# for i in range(n-1):

#     new_dp = [0]* 10


#     for i in range(10):
#         for j in new_path[i]:
#             new_dp[i] += dp[j]

#     dp = new_dp

#     print(new_dp)




# # def getNbr(row, col):
# #     result = []
# #     if row-1 >=0:

# #         if col+2 < len(input[0]):
# #             result.append((row-1,col+2))
        
# #         if col-2 >=0:
# #             result.append((row-1, col-2))


# #     if row+1 < len(input):

# #         if col+2 < len(input[0]):
# #             result.append((row+1,col+2))
        
# #         if col-2 >=0:
# #             result.append((row+1, col-2))

# #     if col-1 >=0:

# #         if row+2 <len(input):
# #             result.append((row+2,col-1))

# #         if row-2 <=0:
# #             result.append((row-2,col-1))
# #     if col+1 < len(input[0]):

# #         if row+2 <len(input):
# #             result.append((row+2,col+1))

# #         if row-2 <=0:
# #             result.append((row-2,col+1))
# #     print(result)
# #     return result

# # for i in range(len(dptable)):
# #     dptable[i][0] = 0
# #     dptable[i][1] = 1


# # counter = 0
# # for row in range(2,len(dptable)):
# #     for col in range(2,len(dptable[0])):
# #         for (i,j) in getNbr(row,col):
# #             counter += dptable[i][j] 
        
# #         dptable[row][col] = counter



