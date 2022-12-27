nums = [1,9,11,5,6,3,2,0]

num1 = [1,3,5,7,9]
num2 = [2,4,6,8,20]

def merge(num1, num2):
    first, second = 0, 0
    first_end, second_end = len(num1)-1, len(num2)-1
    result = []
    while first <= first_end and second <= second_end:
        if num1[first] <= num2[second]:
            result.append(num1[first])
            first += 1
        else:
            result.append(num2[second])
            second += 1
    
    while first <= first_end:
        result.append(num1[first])
        first += 1
    
    while second <= second_end:
        result.append(num2[second])
        second += 1
    return result

def helper(nums, start , end):
    if start >= end:
        return [nums[start]]

    mid = (start + end)//2
    left = helper(nums, start, mid)
    right = helper(nums, mid+1, end)
    return merge(left, right)

print(nums)    
nums = helper(nums, 0, len(nums)-1)
print(nums)



    
