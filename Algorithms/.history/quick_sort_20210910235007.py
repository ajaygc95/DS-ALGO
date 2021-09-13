main_list = [5,7,3,6,4,10,11,9]

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(start, end, arr):
    i = start
    j = end-1
    pivot = start

    while 


def quicksort(start, end, array):
    while start< end:
        pivot = partition(start, end, array)
        quicksort(0,pivot-1,array)
        quicksort(pivot+1, end, array)


print(f"after quick sorting: {main_list}")