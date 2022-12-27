
'''
1. To Find left start:
    a. Check if nums[mid] = left
    b. if nums[mid-1] < left < nums[mid+1]: left start is mid+1
2. To find Right stop
    a. Check if num[mid] == right:
    b. if nums[mid-1] < right < nums[mid+1]
    right stop is mid-1
'''

nums = [2,3,4,5,5,6,7,7]
left = 2
right = 6

left_start = [None]
right_stop = [None]

def find_position(nums, start, end, finding_left):
    while start <= end:
        mid = (start+end)//2

        if nums[mid] == left:
            left_start[0] = mid
            return 
        elif nums[mid-1] < left < nums[mid+1]:
            left_start[0] = mid+1
            return 
        elif left < nums[mid]:
            end = mid-1 
        else:
            start = mid+1

def find_position_right(nums, start, end, target):
    while start <= end:
        mid = (start+end)//2

        if nums[mid] == target and mid-1 >=0 and nums[mid-1] < target:
                right_stop[0] = mid-1
                return 
        elif mid-1 >= 0 and nums[mid] > target and nums[mid-1] < target:
            right_stop[0] = mid-1
            return 1
        elif mid == len(nums)-1 and nums[mid] < target:
            right_stop[0] = mid
            return 
        elif target < nums[mid]:
            end = mid-1
        else:
            start = mid+1
            



find_position(nums, 0,len(nums)-1, True)
find_position_right(nums, 0, len(nums)-1, right)
print(nums[left_start[0]:right_stop[0]+1])

