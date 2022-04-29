input = [5,6,7,9,1,4, 8, 2,3]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def helper(arr, start, end):

    pivot = start
    pivot_point = arr[pivot]

    while start <= end:
        while start <len(arr) and arr[start] <= pivot_point:
            start += 1
        while arr[end] > pivot_point:
            end -= 1

        if start < end:
            swap(arr, start, end)
    swap(arr, pivot, end)
    return end

def quick_sort(arr, start, end):
    if start <= end:
        partition = helper(arr, start, end)
        quick_sort(arr, start, partition-1)
        quick_sort(arr, partition+1, end)

quick_sort(input, 0,len(input)-1)
print(input)

        
        

