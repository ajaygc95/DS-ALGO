input = "leetcode"
words = ["leet", "code"]


dptable =[False] * (len(input)+1)

dptable[0] = True


for i in range(1, len(input)+1):

    for item in range(0, i):
        print("i: ", "item: ", item)
        print(input[i-item-1:i],dptable[i-item-1])

        if input[i-item-1:i] in words and dptable[i-item-1]:
            print("yes")
            dptable[i] = True

print(dptable)






























# hmap = {}
# for word in words:
#     hmap[word] = 1

# dptable = [False] * (len(input)+1)

# for i in range(1,len(dptable)):

#     dptable[i] = (input[:i] in hmap)

#     for lastword in range(1,i):

#         if input[i-lastword:i] in hmap and dptable[i-lastword] == True:
#             dptable[i] = True

# print(dptable) 
# print(dptable[-1])