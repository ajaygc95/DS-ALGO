given_list = [5,7,3,6,4,10,11,9]

def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition(given_list):
    print(given_list)
    start = 1
    end = len(given_list)-1
    pivot = 0

    while start < end:  

        while given_list[start] <= given_list[pivot]:
            start += 1
        while given_list[end] > given_list[pivot]:
            end -= 1

        if start < end:
            swap(start, end, given_list)

    swap(pivot, start-1, given_list)
    
def quicksort()

print(partition(given_list))
print(given_list)