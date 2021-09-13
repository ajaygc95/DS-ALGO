
def swap(i,j , arr):
    print(f"swapping {i} {j}")
    arr[i], arr[j] = arr[j], arr[i]

def partition(start, end, arr):

    i = start
    j = end
    pivot_i = start
    pivot = arr[start]

    while i < j:
        print(i,j)
        while i < len(arr) and arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j =- 1
        
        if i < j:
            swap(i,j ,arr)
            
    swap(end, pivot_i, arr)

    return end

def kth_largest_element(arr, k):
    pass


input = [5, 1, 10, 3, 2]
partition(0, len(input)-1, input)

