main_list = [5,7,3,6,4,10,11,9]

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(start, end, arr):
    i = start
    j = end-1
    pivot = start

    while i < j:
        while i < end and arr[i] < arr[pivot]:
            i += 1
        while j > start and arr[j] > arr[pivot]:
            j -= 1
        
        if i < j:
            swap(i,j,arr)
        
    swap(i,pivot,arr)

    return i


def quicksort(start, end, array):
    while start< end:
        pivot = partition(start, end, array)
        quicksort(0,pivot-1,array)
        quicksort(pivot+1, end, array)


print(f"after quick sorting: {main_list}")