import enum



nums =[ 1,-1,-1,0]

start = 0

result = []

nums.sort()
print(nums)
result = []
def helper(arr,start, end, target):
    print(arr[start:])
    while start < end:

        print(start, end)
        sum1 = arr[start] + arr[end] + target
        print( arr[start], arr[end], target, sum1)
        print()
        
        if arr[start] + arr[end] > target:
            end -= 1
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            result.append([target, arr[start], arr[end] ])
            start += 1
            if arr[start] == arr[start-1] and start < end:
                start += 1

            
final = len(nums) -1

for i , item in enumerate(nums):
    if i > 0 and item == nums[i-1]:
        continue
    print(i, "=======")

    helper(nums, i+1, final, item)
    print()

print(result)

# def helper(arr):

#     for i in range(len(arr)):
#         if i > 0 and arr[i] == arr[i-1]:
#             continue

#         start, end = start + 1, len(arr)-1

#         while start < end:
#             total = arr[start] + arr[i] + arr[end]

#             if 
















# def helper(arr, start, end, target):

#     while start <= end:
#         if arr[start] + arr[end] == target:
#             # result.append([arr[start],arr[end],target])
#             return (arr[start], arr[end])

#         if arr[start] + arr[end] > target:
#             end -= 1
#         if arr[start] + arr[end] < target:
#             start += 1

#     return False



# overall(input)
# print(result)

    












# def overall(arr):
#    arr.sort()

#    for i in range(len(arr)):
#        if 





# store = overall(input)
# print(store)