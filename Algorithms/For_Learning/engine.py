
def outer(input):

    result = []
    def is_pal(arr, a, b):

        if arr[a:b] == arr[a:b][::-1]:
            return True
        else:
            False

    def helper(arr, pos, slate):

        if pos == len(arr):
            result.append("|".join(slate))
            return

        for i in range(pos+1, len(arr)+1):

            if is_pal(arr, pos, i):
                slate.append(arr[pos:i])
                helper(arr, i, slate)
                slate.pop()

        
    helper(input, 0, [])
    return result

input = "abracadabra"

store = outer(input)
print(store)



# def is_pal(arr, a, b):

#     if arr[a:b] == arr[a:b][::-1]:
#         return True
#     else:
#         return False

# input = "abar" 
# print(is_pal(input, 0, len(input)))