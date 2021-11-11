

input = ['a','a','b']


def overall(input):
    input.sort()
    result = []

    def helper(arr, pos, slate):

        if len(arr) == pos:
            result.append(slate[:])
            return

        count = 1

        for j in range(pos, len(arr)):

            if arr[j] != arr[pos]:
                break

            count += 1 

        helper(arr, pos+count, slate)

        for choice in range(0, count+1):
            
            for op in range(choice):
                slate.append(arr[pos])
            helper(arr, pos+count, slate)

            for op in range(choice):
                slate.pop()


    helper(input, 0, [])

    return result

store = overall(input)
print(store)