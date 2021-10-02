
def swap(i,j , arr):
    print(f" index:{i} {j}  swapping {arr[i]}, {arr[j]}")
    arr[i], arr[j] = arr[j], arr[i]


def partition(start, end, array):
    pivot_i = start
    pivot = array[pivot_i]

    i = start
    j = end
    
    while i < j:
        print(i,j)
        print(array)
        while i < len(array) and array[i] <= pivot:
            i += 1
            print(f"i: index: {i}, value: {array[i]}")
        
        while array[j] >= pivot:
            j -= 1
            print(f"j: index: {j}, value: {array[j]}")
        
        if i < j:
            swap(i, j, array)

        print(i,j)

    print(f"pivot element: {array[i]}")
    print(f"i: {i} j: {j} pivot_i: {pivot}")

    swap(j, pivot_i,array)
    print(array)

    return j



def quick_sort(input,start,end,k):

    if start<end:
        pivot = partition(start,end,input)


        print("this is pivot")


    


input = [5, 1, 7,  10, 3, 2, 11]

fonal = quick_sort(input,0,len(input)-1, 3)
print("this is final:" ,fonal)









# def quick_sort(nums, k):

#     pos = partition(0, len(nums)-1, nums)
#     if pos > len(nums) - k:
#         print("==========================",k-(len(nums)-pos)) # 3 - (6-3)
#         return quick_sort(nums[:pos], k-(len(nums)-pos))
#     elif pos < len(nums) - k:
#         return quick_sort(nums[pos+1:], k)
#     else:
#         return nums[pos]