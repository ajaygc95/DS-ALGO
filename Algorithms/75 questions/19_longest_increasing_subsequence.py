given = "raraba"
given2 = [1,2,3]
res = []

def swap(arr, a, b):
    arr[a],arr[b] = arr[b],arr[a]

def helper(arr, pos, slate):
    if len(arr) == pos:
        res.append('|'.join(slate[:]))
        return
    
    for i in range(pos+1, len(arr)+1):
        if arr[pos:i] == arr[pos:i][::-1]:
            slate.append(arr[pos:i])
            helper(arr, i, slate)
            slate.pop()


helper(given, 0,[])

print(res)

