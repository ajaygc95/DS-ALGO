input = "kickstartisawesome"
words = ["kick", "start", "kickstart", "is", "awe", "some", "awesome"]


counter = set(words)


globalcount=[0]
def helper(arr):

    if arr in words: 

        return True

    for i in range(len(arr)):
        for item in range(i):
            if arr[:item] in words and helper(arr[item:]):
                globalcount[0] +=1 
    return 0


helper(input)
print(globalcount[0] % 1000000007)

# print(globalcount[0])


    # if arr in words: 
    #     return True

    # if pos == len(arr):
    #     return 

    # for item in range(len(arr)):

    #     helper(arr[:item], pos+1)
        

    # #     # print(f" position: {item}  first word: {arr[:item]} second word: {arr[item:]}")


    # #     if arr[:item] in words and arr[item:] in words:
    # #         print(f" position: {item}  first word: {arr[:item]} second word: {arr[item:]}")


    # # helper(arr, pos+1)









# dptable = [False]*(len(input)+1)
# dptable[0] = True

# for i in range(1,len(dptable)):

#     for lastword in range(i):

#         print(i, i-lastword-1 , dptable[i-lastword-1], input[lastword:i-lastword-1:])

#         if dptable[i-lastword-1] and input[lastword:i-lastword-1:] in words:
#             dptable[i] = True

# print(dptable)


























# dptable = [False]*(len(input)+1)

# dptable[0] = True


# for i in range(1, len(dptable)):

#     for lastword in range(0,i):
#         print(input[i-lastword-1:i])

#         if dptable[i-lastword-1] and input[i-lastword-1:i] in words:
#             dptable[i] = True


# print(dptable)












































# dptable =[False] * (len(input)+1)

# dptable[0] = True


# for i in range(1, len(dptable)):

#     for item in range(0, i):

#         print(input[i-item-1:i],dptable[i-item-1])
#         if input[i-item-1:i] in words and dptable[i-item-1]:
#             dptable[i] = True

# print(dptable)






























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