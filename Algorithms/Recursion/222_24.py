input = "123"

def output(input,target):
    
    result = []
    def helper(arr, pos, slate, sofar, prevNum):

        if pos == len(arr):
            if sofar == target:
                result.append(slate[:])
            return 

        for i in range(pos, len(arr)):

            prefix = arr[pos:i+1]

            curr_num = int(prefix)

            if prefix[0] == "0":
                return

            if prevNum == None:
                helper(arr, pos+1, slate + prefix, curr_num, curr_num)

            else:
                helper(arr, pos+1, slate + "+" + prefix, sofar+curr_num, curr_num)
                helper(arr, pos+1, slate + "*" + prefix, (sofar-prevNum) + (prevNum*curr_num) , prevNum* curr_num)

    helper(input, 0, "", 0, 0)
    return result

store = output(input, 6)
print(store)




