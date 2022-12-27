nums = [1,9,11,5,6,3,2,0,20]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def helper(nums,start , end):
    pivot_index = start
    pivot_value = nums[pivot_index]

    while start <= end:
        print(start, end)
        while start <= len(nums)-1  and nums[start] <= pivot_value:
            start += 1
        while nums[end] > pivot_value:
            end -= 1

        if start < end:
            swap(nums, start, end)
        
        print(start, end)

    swap(nums, pivot_index, end)
    return end

def quick_sort(nums, start, end):
    if start >= end:
        return 
    
    mid = helper(nums,start, end)
    quick_sort(nums,start, mid-1)
    quick_sort(nums, mid+1, end)
quick_sort(nums, 0, len(nums)-1 )

print(nums)


        



