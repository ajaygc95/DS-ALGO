'''
8,8,8
8,11,13,15

'''

nums = [8,8,8,8]

target = 8
left_value  = [None]
right_value = [None]
def find_position(nums,start,end, finding_left):
    
    while start <= end:
        mid = (start+end)//2    
        if nums[mid] == target:
            if finding_left:
                if mid-1 < 0:
                    left_value[0] = mid
                    return 
                elif mid-1 >= 0 and nums[mid-1] < target:
                    left_value[0] = mid
                    return 
                else:
                    end = mid-1
            else:
                if mid+1 > len(nums)-1:
                    right_value[0] = mid
                if mid+1 <= len(nums)-1 and nums[mid+1] > target:
                    right_value[0] = mid
                    return 
                else:
                    start = mid+1

        elif target < nums[mid]:
            end = mid-1
        else:
            start = mid+1

find_position(nums, 0, len(nums)-1, True)
find_position(nums, 0, len(nums)-1, False)

a, b = left_value[0], right_value[0]
print(a, b)


            
        
        
                    


