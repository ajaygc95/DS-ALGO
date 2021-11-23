
arr = [ 5, 8, 3, 9, 4, 1, 7 ]

# def helper(arr):
#     print(arr)
#     if len(arr) <=1:
#         return arr



#     start = 0
#     end = len(arr)

#     mid = (start+end)//2


#     left = arr[mid:]
#     right = arr[mid:]

#     helper(arr[:mid])
#     helper(arr[mid:])

#     i = j = k = 0
#     aux = []

#     print()
    
#     while i < len(left) and j <len(right):
#         print("+++++++++++++++++++++")
#         print("left",left[i], "right", right[j])
#         print("aux",aux)

#         if left[i] <= right[j]:
#             aux.append(left[i])
#             i += 1
#         else:
#             aux.append(right[j])
#             j += 1
    
#     while i < len(left):
#         aux.append(left[i])
#         i += 1
    
#     while j < len(right):
#         aux.append(right[j])
#         j += 1


#     print("final aux", aux)

# helper(arr)
# print(arr)

def merge_sort(arr):

    if len(arr)<=1:
        return arr

    start = 0
    end = len(arr)
    mid = (start+end)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0


    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            print("This called:",i,j,k)
            arr[k] = left[i]
            i += 1
        else:
            print("else called",i,j,k)
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    print(arr)


merge_sort(arr)
