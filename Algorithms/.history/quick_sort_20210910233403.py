main_list = [5,7,3,6,4,10,11,9]

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition(given_list):
    start = 1
    end = len(given_list)-1
    pivot = 0

    while start < end:  
        print("partition: ", given_list)
        while given_list[start] <= given_list[pivot]:
            start += 1
        while given_list[end] > given_list[pivot]:
            end -= 1

        if start < end:
            swap(start, end, main_list)

    swap(pivot, start-1, main_list)
    return start

def quicksort(start,end,given_list):
    print(given_list)

    if end <= 2:
        return given_list

    pivot = partition(given_list)
    quicksort(0,pivot-1,given_list)
    quicksort(pivot+1,end,given_list)


quicksort(0, len(main_list)-1, main_list)
print(f"this is final list {main_list}")