import re
test_strings = ["test", "test{s}", "xx{y}zz", "m(u|m)"]


# pattern_dict = {
#     'test{s}': 'test, tests',
#     'test(ed|ing)': 'tested, testing',
#     '(b|c(d|e|f))a': 'ba, ca, cda, cea, cfa',
#     'testing\{1,2,3\}': 'test, tests, tested, testing, test3'
# }

# def translate_input_string(input_str, pattern_dict):
#     output_str = input_str
#     for pattern, replacement in pattern_dict.items():
#         output_str = re.sub(pattern, replacement, output_str)
#     return output_str

# print(translate_input_string("test{s}",pattern_dict))


# result = []
# def dfs(arr, pos, slate):

#     if pos == len(arr):
#         result.append(''.join(slate[:]))
#         return 

#     if arr[pos] in ")}":
#         dfs(arr, pos+1, slate)

#     elif arr[pos] == "{":
#         dfs(arr, pos+2, slate)
#         dfs(arr, pos+1,slate)
#     else:
#         dfs(arr, pos+1, slate+[arr[pos]])

# dfs("test{ss}", 0, [])
# print(result )








    


