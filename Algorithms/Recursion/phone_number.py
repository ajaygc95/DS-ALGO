dict1= {
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: ""
    
}

digits = "23"
res = set()
def helper(arr, pos, slate):

    if pos == len(arr):
        res.add(''.join(slate[:]))
        return 

    for i in range(len(arr)):

        for j in range(3):
            slate.append(dict1[int(arr[pos])][j])
            helper(arr, pos+1,slate)
            slate.pop()



helper(digits,0, [])

print(res)


































# hashmap = {

#     "2": "abc",
#     "3": "def",
#     "4": "ghi",
#     "5": "jkl",
#     "6": "mno",
#     "7": "pqrs",
#     "8": "tuv",
#     "9": "wxyz"
#     }

# result= []
# digits = "34"
# def helper(pos, slate):
#     if pos == len(digits):
#         result.append("".join(slate[:]))
#         return

#     if digits[pos] == 1 or digits[pos] == 0:
#         helper(pos+1, slate)
#     else:
#         print(digits[pos])
#         # for item in hashmap[digits[pos]]:

#         #     helper(pos+1, slate + [item] )

# helper(0,[])
# print(result)