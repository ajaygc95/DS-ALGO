import re

given_list = [1,2,5,8]

target = 3


given_list.sort()

for i in range(len(given_list)):

    for j in range(i+1,len(given_list)):
            sum1 = given_list[i] + given_list[j]
            print(sum1)








































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
