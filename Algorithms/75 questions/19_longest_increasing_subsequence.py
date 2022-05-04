from ast import List
from cmath import inf


nums = [0,1,0,3,2,3]
res = []


def helper(arr, pos, prev):
    
    if pos == len(arr):
        return 0
    
    taken = -inf
    
    nottaken = helper(arr, pos+1, prev)
    
    if arr[pos] > prev:
        taken = 1 + helper(arr, pos+1, arr[pos])
    

    return max(taken, nottaken)

print(helper(nums,0,-inf))

