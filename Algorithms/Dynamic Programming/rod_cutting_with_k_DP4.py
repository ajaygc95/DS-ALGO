from socket import IPV6_JOIN_GROUP


input = [[1,5,3],[2,9,4]]

dptable = [[0]*len(input[0]) for _ in range(len(input))]

n = len(input)
k = len(input[0])

dptable[0] = input[0]


for i in range(1,n):

    for j in range(k):

        new_min = 999999

        for x in range(k):
            if x == j:
                continue

            new_min = min(new_min, dptable[i-1][j])
        
        dptable[i][j] = new_min + input[i][j]


# for item in dptable:
#     print(item)

print(min(dptable[-1]))

# min1 = (99999,None)
# min2 = (99999,None)

# for i in range(len(input[0])):

#     if input[0][i] < min1[0]:
#         temp = min1
#         min1 = (input[0][i],i)
#         min2 = temp
#     elif input[0][i] < min2[0]:
#         min2 = (input[0][i],i)



    



# for i in range(len(dptable)):
#     new_min = 9999999
#     for k in range(len(input[0])):

#         if k != min1[1]:
#             if input[i][k] < new_min:
#                 new_min = input[i][k] + min1[0]
#         else:
#             if input[i][k] < new_min:
#                 new_min = input[i][k] + min2[0]




# for i in range(1,len())

# for item in dptable:
#     print(item)

# print(min1)
# print(min2)