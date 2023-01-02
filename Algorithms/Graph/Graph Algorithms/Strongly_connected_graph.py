edges = [[0,1],[1,2],[2,4],[2,3],[3,1],[4,2]]
n = 5
adjlist = [[] for _ in range(5)]

for src, dst in edges:
    adjlist[src].append(dst)

visited = [-1]*n
arrival = [-1]*n
lowestarr = [-1]*n
timestamp = [0]
parent = {}

result = []

def dfs(node):
    visited[node] = 1
    timestamp[0] += 1
    arrival[node] = timestamp[0]
    lowestarr[node] = timestamp[0]

    for nbr in adjlist[node]:
        if visited[nbr] == -1:
            lowestarr[node] = min(dfs(nbr), lowestarr[node])
        else:
            if arrival[nbr] < lowestarr[node]:
                lowestarr[node] = min(arrival[nbr], lowestarr[node])
        
    if lowestarr[node] == arrival[node] and node != 0:
        if not result:
            result.append((node, 0))
            

    
    return lowestarr[node]
dfs(0)

for vertex in range(n):
    if visited[vertex] == -1:
        print(vertex, 0)

print(True if not result else result)

    


