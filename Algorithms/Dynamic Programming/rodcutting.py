#Recursionxx

price = [0,1,3,3,8,9,10]

def helper(pos, price):
    # print(pos)
    if pos == 0: return 0

    result = -1

    for cut in range(1, pos):
        # print(cut,"|--|" , price[cut], end= " |||| ")

        result = max(result, 
        price[cut] + helper(pos-cut, price)

        )
        # print()
    return result


store = helper(6, price)
print("the final IS : ", store)


