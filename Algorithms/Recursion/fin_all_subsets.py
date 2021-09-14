def generate_all_subsets(s):

    final = []
    
    def helper(input , i , subsets):
        if i == len(input):
            final.append("".join(subsets))
            return
        
        helper(input, i+1, subsets)
        subsets += input[i]
        helper(input, i+1, subsets)
        subsets.pop()
    
        
    input = s
    i = 0
    subsets = []
    
    helper(input,i, subsets)
    
    return final

print(generate_all_subsets("XY"))