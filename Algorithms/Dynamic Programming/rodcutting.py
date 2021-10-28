#Recursionxx

price = [1,3,4,8,9,10]

def helper(pos, price):
    if pos == 0: return 0

    result = -1

    for cut in range(1, pos):
        result = max(result, 
        price[cut] + helper(pos-cut, price)
        )
    return result


store = helper(6, price)

print(store)


