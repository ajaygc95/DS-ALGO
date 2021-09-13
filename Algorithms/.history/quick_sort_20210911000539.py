

def swap(a, b, arr):
    print(f"swapping {a} {b}")
    arr[a], arr[b] = arr[b], arr[a]


def partition(start, end, arr):
    
    pivot_i = start
    pivot = arr[pivot_i]

    while start < end:
        print(start, end)

        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, arr)


    print("last swap", start, pivot_i)
    swap(start, pivot_i, arr)
    print(f"after partitionaing : {arr}")
    return start

def quicksort(start, end, array):
    print(array, start, end)
    if start < end:
        pivot = partition(start, end, array)
        quicksort(start, pivot-1, array)
        quicksort(pivot+1, end, array)


main_list = [ 10, 7, 8, 9, 1, 5 ]
quicksort(0, len(main_list)-1, main_list)
print(f"after quick sorting: {main_list}")