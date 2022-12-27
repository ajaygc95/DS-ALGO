phone_number = "1234567"

hash_map = {
"0":"",
"1": "",
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}


result = []
def dfs(pos, slate):

    if pos == 7:
        result.append(slate)
        return 
    if phone_number[pos] == "1" or phone_number[pos] == "0":
        dfs(pos+1, slate)
    else:
        number = str(phone_number[pos])
        for character in hash_map[number]:
            dfs(pos+1, slate+character)


dfs(0, "")
print(result)

