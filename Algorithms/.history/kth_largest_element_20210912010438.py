


def partition(start, end, input):

    i = start
    j = end
    pivot = arr[i]

    while i < j:
        if i < end and arr[i] < pivot:
            i += 1
        else:
            j += 1
        
        if i < j:
            swap(i, j, a)





def kth_largest_element(arr, k):
    pass


input = [5, 1, 10, 3, 2]
partition(0, len(input), input)

