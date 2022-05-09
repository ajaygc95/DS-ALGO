from re import T


candidates = [2,3,6,7]
target = 7

res = []

dptable = [[]] *(target+1)

for i in range(len(dptable)):

    for item in candidates:
        



print(dptable)
print(res)

    
# def helper(arr, slate,target):
#     if target == 0:
#         res.append(slate[:])
#         return
#     if target <=0:
#         return 
#     for i in range(len(candidates)):
#         slate.append(arr[i])
#         helper(arr,slate, target-arr[i])
#         slate.pop()

# helper(candidates,[],target)