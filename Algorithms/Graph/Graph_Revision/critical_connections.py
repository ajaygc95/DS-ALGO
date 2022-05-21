

import collections


edges = [[0,1],[1,2],[2,0],[1,3]]
n = 4

adjlist = [[]for _ in range(n)]

for src, dst in edges:
    adjlist[src].append(dst)
    adjlist[dst].append(src)


visited = [-1] * n
timestamp = [0]
lowestarr = [-1]*n
arrival = [-1]*n
parent = {}

res = []
def dfs(node):
    print(arrival, lowestarr)


    timestamp[0] += 1

    arrival[node] = timestamp[0]
    lowestarr[node] = arrival
    visited[node] = 1

    for nbr in adjlist[node]:
        if visited[nbr] == -1:
            parent[nbr] = node
            lowestarr[node] = min(dfs(nbr), lowestarr[node])
        else:
            if nbr != parent[node]:
                lowestarr[node] = min(arrival[nbr], lowestarr[node])
    if lowestarr[node] == arrival[node] and node != 0:
        res.append((node, parent[node]))

    return lowestarr[node]


dfs(0)
print(res)



