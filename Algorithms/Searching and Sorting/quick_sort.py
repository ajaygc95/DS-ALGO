

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]




input = [ 10, 7, 8, 9, 1, 5 ]


def quicksort(input, start, end, k):

    if start < end:
        pivot = partition(input, start, end)

        if k == pivot:
            print("k found")
            return input[pivot]

        if k >pivot:
                quicksort(input, pivot+1,end, k)
        elif k <pivot:
            quicksort(input, start, pivot-1, k)
            
    return None


def partition(array, start,end):
    pivot_i = start
    pivot = array[start]


    while start < end:


        while start < len(array) and array[start] <= pivot:
            start += 1
        
        while array[end] > pivot:
            end -= 1 

        if start < end:
            swap(array, start, end)
        
    swap(array, pivot_i, end)

    return end

def overall(input):
    quicksort(input,0,len(input)-1,3)


print(overall(input))
print(input)








# def partition(start, end, arr):
    
#     pivot_i = start
#     pivot = arr[pivot_i]

#     while start < end:
#         while start < len(arr) and arr[start] <= pivot:
#             start += 1
#         while arr[end] > pivot:
#             end -= 1

#         if start < end:
#             swap(start, end, arr)


#     print("last swap", arr[end], pivot)
#     swap(end, pivot_i, arr)
#     print(f"after partitionaing : {arr}")
#     return end

# def quicksort(start, end, array):
#     print(array, start, end)
#     if start < end:
#         pivot = partition(start, end, array)
#         quicksort(start, pivot-1, array)
#         quicksort(pivot+1, end, array)


# quicksort(0, len(main_list)-1, main_list)
# print(f"after quick sorting: {main_list}")