a = 63
coins = [1,5,10,25]


dptable = [99999]*(63+1)
dptable[0] = 0


for i in range(1,a+1):
    min_coin = dptable[i]
    for coin in coins:
        if i - coin >= 0:
           dptable[i] = min(dptable[i], dptable[i-coin])

    dptable[i] += 1



























# dptable = [float('inf')] * (a+1)

# dptable[0] = 0

# for i in range(1 ,a+1):

#     for coin in coins:
#         if i-coin >= 0:
#             print(dptable[i], dptable[i-coin])
#             dptable[i] = min(dptable[i], dptable[i-coin])
#     #this one is for adding 1 for itself , ME value. lol
#     dptable[i] += 1

# print(dptable)
# print(dptable[a])
