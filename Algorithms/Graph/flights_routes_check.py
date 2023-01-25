edges =[[1,2],[2,3],[3,1],[1,4],[3,4]]
n = 4

adjlist = [[] for _ in range(n+1)]

for src, dst, in edges:
    adjlist[src].append(dst)

visited = [-1]*(n+1)
timestamp = [0]
arrival = [-1]*(n+1)
lowestarr = [-1]*(n+1)
departure = [-1]*(n+1)

result = []
def dfs(node):
    visited[node] = 1
    timestamp[0] += 1
    arrival[node] = timestamp[0]
    lowestarr[node] = arrival[node]

    for nbr in adjlist[node]:
        if visited[nbr] == -1:
            lowestarr[node] = min(dfs(nbr), lowestarr[node])

        else:
            if departure[nbr] == -1:
                lowestarr[node] = min(lowestarr[node], arrival[nbr])
    
    if lowestarr[node] == arrival[node] and node != 0:
        if not result:
            result.append((node,1))
    
    return lowestarr[node]

components = 0
for v in range(1,n):
    if visited[v] == -1:
        components += 1
        if components > 1:
            if not result:
                print("adding from outer loop")
                result.append((1, v))
        else:
            dfs(v)

print(result)

