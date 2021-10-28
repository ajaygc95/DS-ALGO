input = [1,2,3]

def swap(arr,a,b):
    arr[a],arr[b] = arr[b], arr[a]

def overall(input):
    result = []

    def helper(input,pos, slate):
        # print("helper started")
        if pos == len(input):
            result.append(slate[:])
            return

        for pick in range(pos, len(input)):
            swap(input,pick, pos)
            slate.append(input[pos])
            helper(input, pos+1, slate)
            slate.pop()
            swap(input,pick,pos)
    helper(input,0,[])
    return result

store = overall(input)
for item in store:
    print(item)