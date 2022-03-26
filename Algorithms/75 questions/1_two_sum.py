
coins = [9,1,6]
amount = 11

result = []

def helper(pos, slate, target):

    if target < 0:
        return 

    if target == 0:
        result.append(slate[:])

    
    for coin in coins:
        if target-coin >= 0:

            slate.append(coin)

            helper(pos, slate, target-coin)
            
            slate.pop()


helper(0, [], amount)

print( min(result, key=len))
            


