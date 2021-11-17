input= [1,1,2]


def swap(arr, a, b):
    arr[a],arr[b] = arr[b], arr[a]


def overall(input):
    globalbox = []

    tracker = {}

    def helper(arr, pos, slate):


        if len(arr) == pos:
            globalbox.append(slate[:])
            return 

        tracker = {}
        
        for pick in range(pos, len(arr)):
            if arr[pick] not in tracker:
                tracker[arr[pick]] = True
                swap(arr, pick, pos)
                slate.append(arr[pos])
                helper(arr, pos+1, slate)
                slate.pop()
                swap(arr, pick, pos)

    helper(input,0,[])

    return globalbox


store = overall(input)

for item in store : 
    print(item)











# def overall(input):
#     result = []

#     def helper(arr, pos, slate):

#         if pos == len(arr):
#             result.append(slate[:])
#             return
#         else:
#             hmap = {}
#             for pick in range(pos, len(arr)):
#                 if arr[pick] not in hmap:
#                     hmap[arr[pick]] = True
#                     swap(arr, pick, pos)
#                     slate.append(arr[pos])
#                     helper(arr, pos+1, slate)
#                     slate.pop()
#                     swap(arr, pick, pos)
#     helper(input, 0, [])
#     return result








# def duplicate_combination(nums):
#     result = []
#     def helper(S, pos, slate):
#         if pos == len(S):
#             result.append(slate[:])
#             return

#         hash_map = {}
#         for i in range(pos, len(S)):
            
#             if S[i] not in hash_map:
#                 swap(i,pos,S)
#                 slate.append(S[pos])
#                 helper(S, pos+1, slate)
#                 slate.pop()
#                 swap(i,pos,S)
#                 hash_map[S[i]] = True

#     helper(nums,0,[])
#     return result

# input = [1,2,1]
# to_print = duplicate_combination(input)

# for item in to_print:
#     print(item)