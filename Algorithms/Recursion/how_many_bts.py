def swap(a,b,array):
    array[a], array[b]  = array[b], array[a]
    

def how_many_bts(S):
    result = []

    input = [i for i in range(1,S+1)]

    def helper(S,pos,slate):

        if pos==len(S):
            result.append(slate[:])
            return
        
        for i in range(pos, len(S)):
            swap(pos,i, S)
            slate += [S[pos]]
            helper(S, pos+1, slate)
            slate.pop()
            swap(pos,i,S)
            

    
    helper(input, 0, [])

    return len(result)
input = 3
to_print = how_many_bts(input)
print(f"final:{ to_print}")