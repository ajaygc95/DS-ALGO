from collections import defaultdict
import heapq


dict1 =  {'i love you': 5, 'island': 3, 'iroman': 2, 'i love leetcode': 2}
heap_list = [(value, key) for key,value in dict1.items()]
print(heap_list)

max3 = heapq.nlargest(3, heap_list)
print(max3)


nums = [1,2,3,4,5,7,9]
target = 12

nums.sort()

def twosum(nums, start, end, ):
    while start <= end:
        total = nums[start] + nums[end]
        if total == target:
            return start, end
        elif total < target:
            start += 1
        else:
            end -= 1

result = twosum(nums, 0, len(nums)-1)
print(result)
