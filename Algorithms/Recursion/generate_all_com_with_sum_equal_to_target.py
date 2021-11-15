input = [1,2,3]

target = 3


def overall(input,target):

    globalbox= []

    def helper(arr, pos, slate, sum , target):


        if sum == target:
            globalbox.append(slate[:])
            return
        
        if len(arr) == pos:
            return


        helper(arr, pos+1, slate, sum,  target)
        slate.append(arr[pos])
        helper(arr, pos+1, slate, sum + arr[pos], target)
        slate.pop()

    helper(input, 0, [], 0, 3)
    return globalbox

store = overall(input, target)
print(store)
