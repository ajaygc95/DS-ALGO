

def is_pal(word, left, right):
    print(f"pos: {left} --> '{word[left]}' and i: {right} -->'{word[right]}'")
    while left < right:
        if word[left] is not word[right]:
            return False
            left += 1
            right += 1
        return True

real_final   = []
def palindromic(input, pos, subsets, current_decompostition):

    if pos == len(input):
        print("hello")
        subsets.append(input[pos])
        return 

    for i in range(pos,len(input)):
        print(f"pos: {pos}")
        
        #checking if they are palindrome

        if is_pal(input,pos, i):
            if pos == 0:

                #we are adding input[0:i] so do not put '|' before it. 
                palindromic(input, pos+1, subsets, input[pos:i-pos+1])
            
            else:
                palindromic(input, pos+1, subsets, input[pos:i-pos+1])

    return subsets

input = "abar"

print(palindromic( input, 0, real_final, ""))


