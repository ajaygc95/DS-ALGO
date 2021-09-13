

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(start, end, arr):
    
    pivot_i = start
    pivot = arr[pivot_i]


    while start < end:
        
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, arr)
    swap(start, pivot_i, arr)
    return start


def quicksort(start, end, array):
    if start < end:
        pivot = partition(start, end, array)
        quicksort(0, pivot-1, array)
        quicksort(pivot+1, end, array)


main_list = [5,7,3,6,4,10,11,9]
quicksort(0,len(main_list)-1, main_list)
print(f"after quick sorting: {main_list}")