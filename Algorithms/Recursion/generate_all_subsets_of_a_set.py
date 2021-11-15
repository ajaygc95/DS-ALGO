input = 'xy'




def overall(input):

    globalbox = []

    def helper(arr, pos, slate):

        if len(arr) == pos:
            
            globalbox.append("".join(slate[:]))
            return
        
        helper(arr, pos+1, slate)
        slate.append(arr[pos])
        helper(arr, pos+1, slate)
        slate.pop()
    
    helper(input, 0, [])

    return globalbox


store = overall(input)

print(store)