

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(start, end, arr):
    
    pivot_i = start
    while start < end:
        while start < len(arr) and arr[i] <= pivot:
            i += 1
        while arr[j] > arr[]
    


def quicksort(start, end, array):
    if start < end:
        pivot = partition(start, end, array)
        quicksort(0, pivot-1, array)
        quicksort(pivot+1, end, array)


main_list = [5,7,3,6,4,10,11,9]
quicksort(0,len(main_list)-1, main_list)
print(f"after quick sorting: {main_list}")