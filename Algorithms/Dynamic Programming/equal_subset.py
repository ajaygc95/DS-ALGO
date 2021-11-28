


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



n=6


input = [1,5,11,23]

sum = int(sum(input)/2)

dptable = [False]*(sum+1)




dptable[0] = True


for i in range(len(dptable)):

    for num in input:

        if i - num >=0 and i-num <=len(dptable):

            dptable[i] = dptable[i] or dptable[i-num]
        
        dptable[num] = True



print(dptable)


# result = False or True

# print(result)