from abc import abstractproperty


this = [ 5, 8, 3, 9, 4, 1, 7 ]


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
    aux_list = []

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


merge_sort(this)