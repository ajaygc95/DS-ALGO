input = "a1z"

def overall(input):
    result = []
    def helper(input, pos, slate):

        if pos == len(input):
            result.append(slate)
            return
        
        if input[pos].isdigit():
            helper(input, pos+1, slate + input[pos])
        
        else:
            helper(input,pos+1, slate + input[pos].upper() )
            helper(input,pos+1, slate + input[pos].lower())   


    helper(input,0,"")
    return result

store = overall(input)
print(store)