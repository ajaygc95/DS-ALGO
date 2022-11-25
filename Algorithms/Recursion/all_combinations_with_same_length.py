nums = [1,2,3]

def swap(arr,a,b):
    arr[a],arr[b] = arr[b], arr[a]

res  = []
def helper(arr, position, slate):
    if len(arr) == position:
        res.append(slate[:])
        return 

    for pick in range(position,len(arr)):
        swap(arr, position, pick)
        helper(arr, position+1, slate+[arr[position]])
        swap(arr, position, pick)




helper(nums, 0, [])
print(f"res: {res}")



































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