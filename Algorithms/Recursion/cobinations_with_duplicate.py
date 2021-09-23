
def swap(a, b, arr):
    arr[a],arr[b] = arr[b], arr[a]


def duplicate_combination(nums):
    result = []
    def helper(S, pos, slate):
        if pos == len(S):
            result.append(slate[:])
            return

        hash_map = {}
        for i in range(pos, len(S)):
            
            if S[i] not in hash_map:
                swap(i,pos,S)
                slate.append(S[pos])
                helper(S, pos+1, slate)
                slate.pop()
                swap(i,pos,S)
                hash_map[S[i]] = True

    helper(nums,0,[])
    return result

input = [1,2,1]
to_print = duplicate_combination(input)

for item in to_print:
    print(item)