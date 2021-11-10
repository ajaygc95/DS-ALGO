input = [1,2,3]


def outer(input):

    result = []

    def helper(arr, pos, slate):
        if pos == len(arr):
            result.append(slate[:])
            return 
        
        helper(arr, pos+1, slate)
        slate.append(arr[pos])
        helper(arr, pos+1, slate)
        slate.pop()
    
    helper(input, 0, [])

    return result

store = outer(input)

for item in store:
    print(item)


































# def overall(input):
#     result = []

#     def helper(input, pos, slate):
#         if pos == len(input):
#             result.append(slate[:])
#             return
            
#         helper(input, pos+1, slate)
#         slate.append(input[pos])
#         helper(input, pos+1, slate)
#         slate.pop()
    
#     helper(input,0, [])
#     return result

# store = overall(input)
# print(store)

# print(len(store))




























# # def generate_all_subsets(s):

# #     final = []
    
# #     def helper(input , i , subsets):
# #         if i == len(input):
# #             final.append("".join(subsets))
# #             return
        
# #         helper(input, i+1, subsets)
# #         subsets += input[i]
# #         helper(input, i+1, subsets)
# #         subsets.pop()
    
        
# #     input = s
# #     i = 0
# #     subsets = []
    
# #     helper(input,i, subsets)
    
# #     return final

# # print(generate_all_subsets("XY"))