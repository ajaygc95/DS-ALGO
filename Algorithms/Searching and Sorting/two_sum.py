import re

given_list = [-1,0,1,2,-1,-4]

target = 3


result = set()

def helper(nums, target):
    nums.sort()
    hash_map = {}
    i = 0
    j = len(nums)-1

    while i <= j:
        remaining = target - nums[i]
        if nums[i] in hash_map :
            result.add((target,remaining, nums[i]))
            return
        else:
            hash_map[remaining] = i

        i += 1

for i in range(len(given_list)):
    helper(given_list[i+1:], given_list[i])

print(result)









































# globalbox= []

# def helper(arr, target):

#     start = 0
#     end = len(arr)-1
#     adjlist ={}


#     while start < end:
#         print(adjlist)
#         remaining = target- arr[start]

#         if remaining in adjlist:
#             globalbox.append((adjlist[remaining],start))
#             return
#         adjlist[arr[start]] = start

#         start +=1


# helper(given_list,target)
# print(globalbox)

























# def pair_sum_sorted_array(numbers, target):

#     start = 0
#     right =  len(numbers)-1

#     while start <= right:

#         if numbers[start] + numbers[right] == target:
#             return [start,right]

#         if numbers[start] + numbers[right] > target:
#             right -= 1
#         else:
#             start += 1

# print(pair_sum_sorted_array(given_list,target))
