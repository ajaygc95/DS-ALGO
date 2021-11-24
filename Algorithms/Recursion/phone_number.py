hashmap = {
    1: "abc",
    2: "def",
    3: "ghi",
    4: "jkl",
    5: "mno",
    6: "pqrs",
    7: "tuv",
    8: "wxyz"
}

result= []
digits = "1234567"
def helper(pos, slate):
    if pos == len(digits):
        result.append(slate[:])
        return
    
    for item in hashmap(digits[pos]):

        helper(pos+1, slate + [item] )
    
    

    
 