given_list = [5,7,3,6,4,10,11,9]


def partition(given_list):
    start = 0
    last = len(given_list)-1
    pivot = 0

    while start < last:
        if given_list[start]<= given_list[pivot]:
            

