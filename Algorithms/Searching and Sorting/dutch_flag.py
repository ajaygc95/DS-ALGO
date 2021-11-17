given_list =  ["B", "R","G", "B",'R',"G"]

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def helper(arr):

    r = 0
    g = 0
    b = -1

    for i in range(len(arr)):

        if arr[i] == "R":
            swap(arr, i, r)
            r += 1
        
        if arr[i] == "G":
            pass


helper(given_list)

print(given_list)




























# def dutch_sort(balls):

#     i = 0
#     g = -1
#     r = -1

#     while i < len(balls):
#         if balls[i] == "G":
#             g += 1 #0
#             swap(i,g,balls)
        
#         if balls[i] == "R":
#             g += 1
#             swap(i,g,balls)

#             r += 1
#             swap(r,g,balls)
#         i += 1
# dutch_sort(given_liset)

            




