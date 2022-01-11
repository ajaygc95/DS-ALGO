import random
input =  [6,5,7,4,8,3,9,2,1]
target = 2


def swap(arr, start, end):
    arr[start], arr[end] = arr[end],arr[start]

def helper(arr, start, end, index):

    if start >= end:
        return

    pindex = (start+end)//2
    swap(arr, start, pindex)

    # pindex = start

    pivot = arr[pindex]
    
    left = start

    for i in range(start+1, len(arr)):

        if arr[i] <= pivot:
            left += 1
            swap(arr, i, left)

    swap(arr, start, left)
    helper(arr, start, left, index)
    helper(arr, left+1, end, index)

    # if index == left:
    #     return 
    # elif index > left:
    #     helper(arr, start, left, index)
    # else:

    #     helper(arr, left+1, end, index)


def quick_sort(arr,k):
    helper(arr,0,len(arr)-1,len(arr)-1)
    # return arr[len(arr)-1]
print(input)
store = quick_sort(input, 2)
print(input)
print(store)

























# def helper(array, start, end):
      
#     # Initializing pivot's index to start
#     pivot_index = start 
#     pivot = array[pivot_index]
      
#     while start < end:
          
#         while start < len(array) and array[start] <= pivot:
#             start += 1
              
#         while array[end] > pivot:
#             end -= 1
          
#         if(start < end):
#             array[start], array[end] = array[end], array[start]
      

#     array[end], array[pivot_index] = array[pivot_index], array[end]

#     return end

# def quick_sort(arr, start, end, k):

#     partition = helper(arr, start, end)
#     print(partition)

#     if partition == k:
#         return arr[partition]
#     elif partition < k:
#         return quick_sort(arr, partition+1, end, k)
#     else:
#         return quick_sort(arr, start, partition-1, k)
        

# store = quick_sort(input, 0, len(input)-1, len(input)-2)
# print(input)
# print(store)













# # def helper(input,start, end):
    

# #     pivot = start
# #     pivot_val = input[pivot]

# #     while start < end:
        
# #         if start < len(input) and input[start] <= pivot_val:
# #             start += 1

# #         if input[end] > pivot_val:
# #             end -= 1

# #         if start < end:
# #             swap(input, start, end)

# #     swap(input, pivot, end)

# #     return end

# # def quickSort(start, end, array,k):
# #     # print(array, start, end)

# #     if start < end:
# #         pivot = helper(array, start, end)
# #         print(pivot)

# #         if pivot < len(array)-k:
# #             return quickSort(start, pivot-1, array, len(array)-k)

# #         elif pivot > len(array)-k:

# #             return quickSort(pivot+1, end, array, len(array)-k)
# #         else: 
# #             return array[pivot]





# # store = quickSort(0, len(input)-1, input, len(input)-5)
# # print(input)
# # print(store)



















# # def quick_sort(nums, k):

# #     pos = helper(nums, 0, len(nums)-1)
# #     if pos > len(nums) - k:
# #         print("==========================",k-(len(nums)-pos)) # 3 - (6-3)
# #         return quick_sort(nums[:pos], k-(len(nums)-pos))
# #     elif pos < len(nums) - k:
# #         return quick_sort(nums[pos+1:], k)
# #     else:
# #         return nums[pos]

























# # def swap(i,j , arr):
# #     print(f" index:{i} {j}  swapping {arr[i]}, {arr[j]}")
# #     arr[i], arr[j] = arr[j], arr[i]


# # def partition(start, end, array):
# #     pivot_i = start
# #     pivot = array[pivot_i]

# #     i = start
# #     j = end
    
# #     while i < j:
# #         print(i,j)
# #         print(array)
# #         while i < len(array) and array[i] <= pivot:
# #             i += 1
# #             print(f"i: index: {i}, value: {array[i]}")
        
# #         while array[j] >= pivot:
# #             j -= 1
# #             print(f"j: index: {j}, value: {array[j]}")
        
# #         if i < j:
# #             swap(i, j, array)

# #         print(i,j)

# #     print(f"pivot element: {array[i]}")
# #     print(f"i: {i} j: {j} pivot_i: {pivot}")

# #     swap(j, pivot_i,array)
# #     print(array)

# #     return j



# # def quick_sort(input,start,end,k):

# #     if start<end:
# #         pivot = partition(start,end,input)


# #         print("this is pivot")


    


# # input = [5, 1, 7,  10, 3, 2, 11]

# # fonal = quick_sort(input,0,len(input)-1, 3)
# # print("this is final:" ,fonal)









# # def quick_sort(nums, k):

# #     pos = partition(0, len(nums)-1, nums)
# #     if pos > len(nums) - k:
# #         print("==========================",k-(len(nums)-pos)) # 3 - (6-3)
# #         return quick_sort(nums[:pos], k-(len(nums)-pos))
# #     elif pos < len(nums) - k:
# #         return quick_sort(nums[pos+1:], k)
# #     else:
# #         return nums[pos]