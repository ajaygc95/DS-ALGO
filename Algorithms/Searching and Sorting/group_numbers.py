given_list = [3,1,2,5,4,6]

def swap(arr, a,b):
    arr[a],arr[b] = arr[b], arr[a]


def helper(input,start, end):

    while start < end:

        if input[start]%2==0:
            start += 1
        if input[end]%2==1:
            end -= 1
        
        if start < end:
            swap(input,start, end)
    
helper(given_list, 0, len(given_list)-1)
print(given_list)















# def solve(arr):
#     i = 0
#     j = len(arr)-1

#     while i <= j:
#         if arr[i]%2 ==0:
#             i += 1
#         else:
#             if arr[j]%2 == 0:
#                 swap(i,j,arr)
#                 j -=1 
#             else:
#                 j -= 1
        

# solve(given_list)
# print(given_list)