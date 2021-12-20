input = ["a","a","b"]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


globalbox = []
def helper(arr, pos, slate):

    if pos == len(arr):
        globalbox.append(slate[:])
        return 
    
    count = 0

    for index in range(pos, len(arr)):
        if arr[index] != arr[pos]:
            break
        count += 1
    
    helper(arr,pos+1,slate)

    for copies in range(1, count):
        slate.append(arr[pos])
        helper(arr, pos+count, slate)

    for c in range(1, count):
        slate.pop()

helper(input, 0, [])

for item in globalbox:
    print(item)