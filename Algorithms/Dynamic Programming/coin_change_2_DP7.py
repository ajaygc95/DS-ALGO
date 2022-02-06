def change(self, amount: int, coins: List[int]) -> int:

    dptable = [[0]*(amount+1) for _ in range( len(coins))]

    for i in range(len(dptable)):
        dptable[i][0] = 1

    for i in range(len(dptable)):
        for amount in range(1, len(dptable[0])):
            
            dptable[i][amount] = dptable[i-1][amount]
            
            if amount - coins[i] >= 0:
                dptable[i][amount] += dptable[i][amount-coins[i]] 
                
    return dptable[-1][-1]