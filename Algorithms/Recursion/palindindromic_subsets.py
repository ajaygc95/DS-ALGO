real_final = []

def palindromic(input,i, subsets):

    if len(input) == i:
        w = ""
        for i in subsets:
            w = i + w
        print("".join(subsets) ,w)

        if "".join(subsets) == w:
            print(subsets)
            final_word = ''.join(subsets)
        else:
            final_word = '|'.join(subsets)
        real_final.append(final_word)
        return
    
    palindromic(input, i+1, subsets)
    subsets += input[i]
    palindromic(input, i+1, subsets)
    subsets.pop()


input = "abracadabra"

palindromic(input, 0, [])

print(real_final)