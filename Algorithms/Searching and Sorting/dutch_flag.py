given_list =  ["B", "R","G", "B",'R',"B"]

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]



def helper(arr):

    total_len = len(arr)-1

    start = 0
    middle= 0
    end = total_len

    while middle <= end:

        print(arr[middle])
        if arr[middle] == 'R':
            swap(arr, middle, start)
            start += 1

        if arr[middle] == "B":
            swap(arr, middle, end)
            end -= 1

            if arr[middle] == "R":
                swap(arr,middle,start)
                start += 1

        middle += 1

helper(given_list)
print(given_list)



# def helper(arr):

#     r = 0
#     g = 0
#     end = -1

#     for i in range(len(arr)):

#         if arr[i] == "R":
#             swap(arr, i, r)
#             r += 1
        
#         if arr[i] == "G":
#             pass


# helper(given_list)

# print(given_list)


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

            




