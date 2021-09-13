given_list = [5,7,3,6,4,10,11,9]

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition(given_list):
    
    start = 0
    last = len(given_list)-1
    pivot = 0

    while start < last:

        if given_list[start]<= given_list[pivot]:
            start += 1
        if given_list[last] > given_list[pivot]:
            last -= 1

        swap(start,pivot, given_list)
    print()
    return given_list[start]

def quicksort(given_list):
    print(given_list)

    start = 0
    end = len(given_list)-1
    print(start, end)

    while start < end:

        pivot = partition(given_list)
        quicksort(given_list[:pivot])
        quicksort(given_list[pivot:])

quicksort(given_list)
print(given_list)
