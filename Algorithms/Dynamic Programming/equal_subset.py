'''
            (0, 7)
        (1,6)       (1,7)
    (2,4)   (2,6)
(3,0) (3,4)                    

'''

# arr = [10, -3, 7, 2, 1, 3]

arr = [1,2,4,5]

total = sum(arr)
target = int(total/2)


dptable = [[False]*(target+1) for _ in range(len(arr))]


for i in range(len(dptable)):
    dptable[i][0] = True




# for item in dptable:
#     print(item)








# dptable = [[False]*(target + 1) for _ in range(len(arr)+1)]

# for i in range(len(dptable)):
#     dptable[i][0] = True

# for item in dptable:
#     print(item)

# for pos in range(1,len(dptable)):

#     for target in range(len(dptable[0])):

#         result = None

#         if target >= arr[pos-1]:
#             result = dptable[pos-1][target-arr[pos-1]]

#         dptable[pos][target] = result or dptable[pos-1][target]

#     print()
# for item in dptable:
#     print(item)



# dict1 = [[False]]

# def helper(arr, pos, target):
    
#     if target == 0:
#         return True

#     if len(arr) == pos:
#         return 

#     result = helper(arr, pos+1, target) or helper(arr, pos+1, target-arr[pos])

#     dict1[pos][target] 
#     return result


# dptable = [[False]*(target + 1) for _ in range(len(arr)+1)]

# for i in range(len(dptable)):
#     dptable[i][0] = True

# for item in dptable:
#     print(item)

# for pos in range(1,len(dptable)):

#     for target in range(len(dptable[0])):

#         result = None

#         if target >= arr[pos-1]:
#             result = dptable[pos-1][target-arr[pos-1]]
#         dptable[pos][target] = result or dptable[pos-1][target]
#     print()
# for item in dptable:
#     print(item)


# store = helper(arr, 0, total)
# print(store)


# dptable = [[False]*(target+1) for _ in range(len(arr))]


# for i in range(len(dptable)):

#     dptable[i][0] = True

# # There are multiple partitionings where s1 sums up to 10 and s2 sums up to 10; they are all correct answers:

# # s1 = [ 10 , -3 , 3 ] and s2 = [ 7 , 2 , 1 ] (Sample output)
# # s1 = [ 7 , 2 , 1 ] and s2 = [ 10 , -3 , 3 ]
# # s1 = [10] and s2 = [-3, 3, 7, 2, 1]
# # s1 = [-3, 3, 7, 2, 1] and s2 = [10]
# # s1 = [10, -3, 2, 1] and s2 = [7, 3]
# # s1 = [7, 3] and s2 = [10, -3, 2, 1]


# sum = sum(input)
# target = sum/2
# dptable =[0]*(sum+1)
# dptable[0] = 0
#USING RECURSION

# globalbox = []

# def helper(arr, pos, target, slate):
#     if target == 0:
#         return True
#         # if slate[:] not in globalbox:
#         #     globalbox.append(slate[:])

#     if len(arr) == pos:
#         return False

#     return helper(arr, pos+1, target, slate) or helper(arr, pos+1, target-arr[pos], slate + [arr[pos]])


# store = helper(input, 0, 10, [])
# print(store)


#Recursion Formula is f(pos, target) = f(pos+1, target) or f(pos+1, target-arr[pos])



# print(sum)
# dptable = [[False]*(sum+1) for _ in range(len(input)+1)]


# for i in range(len(dptable)):
#     dptable[i][0] = True


# for item in dptable:
#     print(item)


# n=6


# input = [10, -3, 7, 2, 1, 3]

# sum = int(sum(input)/2)

# dptable = [False]*(sum+1)


# dptable[0] = True



#     # for item in input:
#     #     if i-item >=0 and (i-item <len(dptable) and not dptable[i]):
            
#     #         dptable[i] = dptable[i-item]
    
# print()    
# print(dptable)


# n=6


# input = [1,5,11,5]
# print(sum(input))
# sum = int(sum(input)/2)


# dptable = [[False]*(sum+1) for _ in range(len(input)+1)]

# for i in range(len(dptable)):
#     dptable[i][0]= True

# # for i in range(len(dptable[0])):
# #     print(f"  {i}....", end="")

# print()


# for  item in range(len(input)):
#     print(item)

#     for i in range(1, len(dptable)):
#         # # print(f"  {i} ", end="...")
#         # print(i,sum-input[item])
#         # # print(dptable[i][1])
        
#         if 0 <= sum-input[item] < sum:
#             dptable[item][i] = dptable[i-1][sum-input[item]] or dptable[i-1][sum]


# for pos in range(len(input)-1, -1, -1):
#     print(pos)

#     for target in range(1, len(dptable[0])):

#         if input[pos] <= target:

#             dptable[pos][target] = dptable[pos+1][target-input[pos]] or dptable[pos+1][target]

# for item in dptable:
#     print(item)