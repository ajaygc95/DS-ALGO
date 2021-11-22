word1 = "eq"

word2 = "eqqqqqqqq"

dptable = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

for i in range(len(dptable)):
    dptable[i][0] = i

for j in range(1,len(dptable[0])):
    dptable[0][j] = j


for item in dptable:
    print(item)

for row in range(1,len(dptable)):
    for col in range(1,len(dptable[0])):
        
        print(word1[row-1], word2[col-1])

        # if word1[row-1] == word2[col-1]:
        #     adder = 0
        # else: adder = 1

        dptable[row][col] = min(
            dptable


        )

        print(dptable)

for item in dptable:
    print(item)

print(dptable[-1][-1])






































# dptable = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]


# for i in range(1, len(word2)+1):
#     dptable[0][i] = i

# for j in range(1, len(word1)+1):
#     dptable[j][0] = j


# for item in dptable:
#     print(item)

# for row in range(1,len(dptable)):
#     for col in range(1,len(dptable[0])):

#         x = 0 if word1[row-1] == word2[col-1] else 1

#         dptable[row][col] = min(

#                 dptable[row-1][col] + 1,
#                 dptable[row][col-1] + 1,

#                 dptable[row-1][col-1] + x
#         )
 
#     print()

# print(dptable[-1][-1])