input = "rada"

def overall(input):
    globalbox = []

    def helper(arr, pos, slate):

        if len(arr) == pos: 
            globalbox.append("|".join(slate[:]))
            return

        for i in range(pos+1, len(arr)+1):

            if  arr[pos:i] == arr[pos:i][::-1]:
                slate.append(arr[pos:i])
                helper(arr, i, slate)
                slate.pop()

    helper(input, 0, [])
    return globalbox


store = overall(input)

for item in store:
    print(item)






