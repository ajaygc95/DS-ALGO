input = ["a","a","b"]

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


globalbox = []
def helper(arr, pos, slate):

    if pos == len(arr):
        globalbox.append(slate[:])
        return 

    count = 1

    for index in range(pos, len(arr)):
        if arr[index] != arr[pos]:
            break
        count += 1
    print(count)
    #exclude decision
    helper(arr, pos+count, slate)

    #include decision

    for copies in range(0, count+1):

        for op in range(copies):
            slate.append(arr[pos])

        helper(arr, pos+count, slate)

        for op in range(copies):
            slate.pop()


input.sort()
helper(input, 0, [])

for item in globalbox:
    print(item)