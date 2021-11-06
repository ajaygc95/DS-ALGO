#Recursionxx

input= [3,7,2,6,6]


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

