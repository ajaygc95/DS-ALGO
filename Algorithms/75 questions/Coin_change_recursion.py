adjlist = [[11,12,13,14],[21,22,23,24],[31,32,33,34]
    ]

clone = [[0]*len(adjlist) for _ in range(len(adjlist[0]))]


for i in range(len(adjlist)):
    for j in range( len(adjlist[0])):
        clone[j][i] = adjlist[i][j]


for i in range(len(clone)):
    clone[i][0], clone[i][-1] = clone[i][-1], clone[i][0]
for item in clone :
    print(item)

            


