given_list = [5,7,3,6,4,10,11,9]

def (a, b, arr):
    arr[a]

def partition(given_list):
    start = 0
    last = len(given_list)-1
    pivot = 0

    while start < last:

        if given_list[start]<= given_list[pivot]:
            start += 1
        if given_list[last] >= given_list[pivot]:
            last -= 1
        
        swap(start,pivot, given_list)



