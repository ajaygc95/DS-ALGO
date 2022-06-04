input = "26"
def helper(n):
    if n == 0:
        return 0
    
    helper(n-1)

helper(len(input))

# nums = [1, 5, 8, 9]

# dptable = [0]*(len(nums)+1)
# dptable[0] = 0
# dptable[1] = nums[0]

# for i in range(2, len(dptable)):
#     for j in range(1, i):
#         dptable[i] = max(nums[j]+dptable[i-j-1], dptable[i])

# print(dptable)



    
# res = [0]

# def helper(arr, pos, sum):
    
#     if pos > len(arr):
#         return 
    
#     if len(arr) == pos:
#         res[0] = max(res[0], sum)
#         return 
    
#     for i in range(1,len(arr)):
        
#         helper(arr, pos+i, sum+arr[i-1])
    
# helper(price, 0, 0)
# print(res)





































# dptable = [0]*n 

# dptable[0] = 0
# dptable[1] = price[0]

# for i in range(2, n):

#     for j in range(1, i):

#         dptable[i]  = max(price[j] + dptable[i-j],dptable[i])

# print(dptable[i])