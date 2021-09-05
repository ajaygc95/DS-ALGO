arr1 = [1 ,3, 5]
arr2 = [2, 4, 6, 0, 0, 0]


def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #

    i =j =  len(arr1) -1
    k = len(arr2)-1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr2[k] = arr1[i]
            i -= 1
        else:
            arr2[k] = arr2[j]
            j -= 1
        k -= 1

    while i >= 0:
        arr2[k] = arr1[i]
        i -= 1
        k -= 1
    while j >= 0:
        arr2[k] = arr2[j]
        j -= 1
        k -= 1



merger_first_into_second(arr1,arr2)
print(arr2)
    
