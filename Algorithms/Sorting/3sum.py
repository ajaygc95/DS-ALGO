input = [-1,0,1,2,-1,-4]

arr = [1, 3, 4, 5, 7, 8, 9]

start = 0
end = len(arr)-1
target = 8




def helper(arr, start, end,target):
    while start < end:

        if arr[start] + arr[end] == target:
            return (arr[start],arr[end])
        
        if arr[start] + arr[end] > target:
            end -= 1
        if arr[start] + arr[end] < target:
            start += 1
    return False

def overall(arr):
    end = len(arr)-1
    for i in range(len(arr)-1):
        return (i,helper(arr[i:end],0,len(arr[i:end])-1,-(i)))

store = overall(input)
print(store)