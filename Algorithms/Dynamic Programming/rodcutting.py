#Recursionxx

input= [3,7,2,6,6]


#Identify Table

dptable = [0]*(len(input)+1)

dptable[0] = 0
dptable[1] = input[0]

print(dptable)

for i in range(2, len(dptable)):
    max_in = -1

    for j in range(1, i):
        max_in = max(dptable[i-j] + dptable[j], input[i-1])

    dptable[i]  = max_in


print(dptable)




























# dptable = [0] * (len(input)+1)

# dptable[0] = 0
# dptable[1] = 1

# def helper(input):

#     if len(input) == 0:
#         return 0

#     result = -1

#     for cut in range(1, len(input)):
        








































#Identify A table:


def rodcut(prices):
    rodlen = len(prices) + 1
    dptable = [None] * rodlen
    dptable[0] = 0
    dptable[1] = prices[0]

    for length in range(2, rodlen):
        result = prices[length-1]
        for cut in range(1, length):
            result = max(result, dptable[cut] + dptable[length-cut])
        dptable[length] = result









rodcut(input)




































# price = [1,3,4,8,9,10]

# def helper(pos, price):
#     if pos == 0: return 0

#     result = -1

#     for cut in range(1, pos):
#         result = max(result, 
#         price[cut] + helper(pos-cut, price)
#         )
#     return result


# store = helper(6, price)

# print(store)


