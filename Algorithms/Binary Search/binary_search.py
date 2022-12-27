nums = [1,2]
target = 1
def binary_search(start, end):

    while start <= end:
        mid = (start+end)//2
        print(nums[mid])
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            end = mid-1
        else:
            start = mid+1

    return False


result = binary_search(0, len(nums)-1)
print(result)