


def overall(input,k):
    result = []

    def helper(arr, pos, slate,k):

        if len(slate) == k:
            result.append(slate[:])
            return

        if pos == arr:
            return 
        
        helper(arr, pos+1, slate,k)

        slate.append(pos)
        helper(arr, pos+1, slate, k)
        slate.pop()
    
        

    helper(input, 0,[],k)
    return result

store = overall(6,2)
print(store)

