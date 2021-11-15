input = [1,2,3]
amount = 3


#recursive way

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

globalSum = []
globalbox = []
def helper(arr, pos, slate, k):

    if pos == k:
        globalSum.append(slate[:])

    if len(arr) == pos:
        globalbox.append(slate[:])
        return 

    helper(arr, pos+1, slate, k-arr[pos])
    slate.append(arr[pos])  
    helper(arr, pos+1, slate, k-arr[pos])


store = helper(input,0,[], 3)

# print(globalbox)
print(globalSum)



















# input = [1,2,3]
# amount  = 3

# dptable= [0]*(amount+1)
# dptable[0] = 1

# for i in range(1, len(dptable)):

#     for coin in input:
#         if coin >=0:
#             dptable[i] = dptable[i-coin] + dptable[i]

# print(dptable[-1])

