main_list = [5,7,3,6,4,10,11,9]

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition(left, right,given_list):
    print(given_list , left, right)
    start = left
    end = right
    pivot = start

    while start < end:  
        print("partition: ", given_list)
        while start < end and given_list[start] <= given_list[pivot]:
            start += 1
        while end > left and given_list[end] > given_list[pivot]:
            end -= 1

        if start < end:
            swap(start, end, main_list)

    if given_list[start] > pivot:
    swap(pivot, start-1, main_list)
    return start

def quicksort(start,end,given_list):
    print("inside quick sort", given_list)
    print("end and start:",start, end)
    if start < end:
        pivot = partition(start, end,given_list)
        quicksort(0, pivot-1, given_list)
        quicksort(pivot+1, end, given_list)


quicksort(0, len(main_list)-1, main_list)
print(f"this is final list {main_list}")