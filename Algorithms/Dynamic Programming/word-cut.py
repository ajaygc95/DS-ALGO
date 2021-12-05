input = "kickstartisawesome"
words =  ["kick", "start", "kickstart", "is", "awe", "some", "awesome"]




dptable = [0]*(len(input)+1)
dptable[0] = 1


for i in range(1, len(dptable)):

    # print("===============")
    for word in range(i):

        # print(word, input[:word], "|", input[word:i] , dptable[word])

        if dptable[word] and input[word:i] in words:
            dptable[i] += dptable[word]

    print()

print(end="       ")
for item in input:
    print( f"{item}..... ", end="")
print()
print(dptable)

# total_len = len(input)

# globalcount = [0]

# aux = {}

# def helper( arr, pos=0):


#     if arr in aux :
#         return 
#     if pos == len(arr):
#         globalcount[0] += 1
#         return 

#     for i in range(pos, len(arr)+1):

#         if arr[pos:i] not in aux:
#             aux[arr[pos:i]] = True

#         if arr[pos:i] in words:
#             helper(arr, i)



# helper(input)
# print(globalcount[0] )

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