input = "a1z"

# globalbox = []
# def helper(arr, pos, slate):

#     if len(arr) == pos:
#         globalbox.append(''.join(slate[:]))
#         return
    
#     if arr[pos].isdigit():
#         helper(arr,pos+1, slate + [arr[pos]])
#     else:
#         helper(arr, pos+1, slate +[arr[pos].upper()])
#         helper(arr, pos+1, slate +[arr[pos].lower()])


# helper(input,0,[])

# print(globalbox)




































s = "a1b2"

for i in range(len(s)):
    if s[i].isdigit():
        print(s[i])


























# def overall(input):
#     result = []
#     def helper(input, pos, slate):

#         if pos == len(input):
#             result.append(slate)
#             return
        
#         if input[pos].isdigit():
#             helper(input, pos+1, slate + input[pos])
        
#         else:
#             helper(input,pos+1, slate + input[pos].upper() )
#             helper(input,pos+1, slate + input[pos].lower())   


#     helper(input,0,"")
#     return result

# store = overall(input)
# print(store)