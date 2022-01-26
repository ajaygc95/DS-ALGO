
graph = {

    0 : [4,6],
    1 : [6,8],
    2 : [7,9],
    3 : [4,8],
    4 : [3,9,0],
    5 : [],
    6 : [0,1,7],
    7 : [2,6],
    8 : [3,1],
    9 : [4,2]


}
n = 4
dptable = [[0]*n for _ in range(10)]

for i in range(len(dptable)):
    dptable[i][0] = 1


for i in range(n):

    for j in range(10):
        for num in graph[j]:
            dptable[j][i] += dptable[num][i-1]

print(dptable[-1][-1])