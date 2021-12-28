def is_pal(word, left, right):

    # print(f"pos: {left} --> '{word[left]}' and i: {right} -->'{word[right]}'")
    word1 = word[left:right]

    # print(f"word: {word1} len: {len(word1)}")

    if len(word1) == 0:
        return False

    if word1 == word1[::-1]:
        # print("y_pali", word1)
        return True
    else:
        return False


real_final   = []
input = "abar"


def palindromic_decomposition(arr, pos, slate):

    if pos == len(arr):
        real_final.append("|".join(slate[:]))
        return  

    for i in range(pos+1, len(arr)+1):
        if  is_pal(arr, pos, i):
            slate.append(arr[pos:i])
            palindromic_decomposition(arr, i, slate)
            slate.pop()

palindromic_decomposition(input,0,[])
print(real_final)

























# def palindromic(input, pos, subsets, current_decompostition):

#     if pos == len(input):
#         subsets.append(current_decompostition)
#         return 

#     for i in range(pos,len(input)):
#         # print(pos,input[pos:i])
#         #checking if they are palindrome

#         if is_pal(input,pos, i):
#             if pos == 0:
#                 print("position 0")
#                 #we are adding input[0:i] so do not put '|' before it. 
#                 palindromic(input, pos+1, subsets, input[pos:i-pos+1])
            
#             else:
                
#                 palindromic(input, pos+1, subsets,  current_decompostition  + "|" + input[pos:i-pos+1])

#     return subsets

# input = "abar"

# print(palindromic( input, 0, real_final, ""))


