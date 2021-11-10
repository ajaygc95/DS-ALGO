input = [1,2,3]

def swap(arr,a,b):
    arr[a],arr[b] = arr[b], arr[a]


def outer(input):

    result = []
    def helper(arr, pos, slate):

        if pos == len(arr):
            result.append(slate[:])
            return
        
        for item in range(pos, len(arr)):
            swap(arr, item, pos)
            slate.append(arr[pos])
            helper(arr, pos+1, slate)
            slate.pop()
            swap(arr ,item,pos)
    
    helper(input, 0, [])

    return result

store = outer(input)
print(store)
































# def overall(input):
#     result = []

#     def helper(input,pos, slate):
#         # print("helper started")
#         if pos == len(input):
#             result.append(slate[:])
#             return

#         for pick in range(pos, len(input)):
#             swap(input,pick, pos)
#             slate.append(input[pos])
#             helper(input, pos+1, slate)
#             slate.pop()
#             swap(input,pick,pos)
#     helper(input,0,[])
#     return result

# store = overall(input)
# for item in store:
#     print(item)