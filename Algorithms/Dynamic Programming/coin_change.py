a = 63
coins = [1,5,10,21,25]


dptable = [999999] * (a+1)

dptable[0] = 0

for i in range(1,len(dptable)):
    min_value = dptable[i]

    for coin in coins:
        if i - coin >= 0:
            min_value = min(min_value, dptable[i-coin])
        
    dptable[i] = min_value + 1

print(dptable)































# dptable = [99999999]*(a+1)
# dptable[0] = 0
# dptable[coins[0]] = 1

# for i in range(1, len(dptable)):
#     for item in coins:

#         if i -item >=0:
#             dptable[i] = min(dptable[i-item], dptable[i])

#     dptable[i] += 1

# for i,j in enumerate(dptable):
#     print(i,j)



































# dptable = [99999]*(63+1)
# dptable[0] = 0


# for i in range(1,a+1):
#     min_coin = dptable[i]
#     for coin in coins:
#         if i - coin >= 0:
#            dptable[i] = min(dptable[i], dptable[i-coin])

    # dptable[i] += 1



























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
