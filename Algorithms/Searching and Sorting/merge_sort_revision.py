arr = [ 5, 8, 3, 9, 4, 1, 7 ]

def helper(arr, start, end):

    print(arr[start:end])

    if start == end:
        return 

    mid = (start + end)//2

    left = arr[:mid]
    right = arr[mid:]

    helper(arr,start,mid)
    helper(arr, mid+1, end)

    i = j = 0
    k = 0
    aux = []

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            aux.append(left[i])
            i += 1
            k += 1
        else:
            aux.append(right[j])
            j += 1
            k += 1
    while i < len(left):
        aux.append(left[i])
        i += 1
    
    while j < len(right):
        aux.append(right[j])
        j += 1


helper(arr, 0, len(arr))