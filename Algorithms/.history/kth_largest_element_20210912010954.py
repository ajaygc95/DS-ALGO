
def swap(i,j , arr):
    print(f"swapping {i} {j}")
    arr[i], arr[j] = arr[j], arr[i]

def partition(start, end, arr):

    i = start
    j = end
    pivot = arr[start]

    while i < j:

        while i < len(arr) and i <= pivot:
            i += 1
        whiel arr[j]



    return end





def kth_largest_element(arr, k):
    pass


input = [5, 1, 10, 3, 2]
partition(0, len(input)-1, input)

