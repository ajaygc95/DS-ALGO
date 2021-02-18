# def twosums(nums,target):
#     ilist = [2,7,11,15]
#     wlist = []
#     idict = {}
#     for i in range(0,len(nums)):
#         k = target - nums[i]

#         if k not in idict:
#             idict[nums[i]] = i
#         if k in idict:
#             return i, idict[k]

#     return idict

# ilist = [2,7,11,15]
# target = 9

# toprint = twosums(ilist, target)
# print(toprint)


list1 = [1,2,3,4]
my_lst = ''.join(map(str,list1))
print(my_lst)