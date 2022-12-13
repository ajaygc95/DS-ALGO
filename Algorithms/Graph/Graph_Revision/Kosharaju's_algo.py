import heapq

edges = [[1,2],[2,3],[3,1],[3,4],[4,5],[5,4]]
n = 5

adjlist = [[] for _ in range(n+1)]

for src, dst in edges:
    adjlist[src].append(dst)

print(adjlist)

visited = [-1]*(n+1)
timestamp = [0]
departure =[-1]*(n+1)
topsort = []

def dfs(node):
    visited[node] = 1

    for nbr in adjlist[node]:
        if visited[nbr] ==-1:
            dfs(nbr)
    


    timestamp[0] += 1
    departure[node] = timestamp[0]
    topsort.append(node)

for v in range(1, n+1):
    if visited[v] == -1:
        dfs(v)

adjlist_reversed = [[] for _ in range(n+1)]

for vertex in range(n+1):
    for nbr in adjlist[vertex]:
        adjlist_reversed[nbr].append(vertex)

visited_reversed = [-1]*(n+1)
result1 = [-1]*(n+1)

def dfs_reversed(node, sccid):
    visited_reversed[node] = sccid

    for nbr in adjlist_reversed[node]:
        if visited_reversed[nbr] == -1:
            dfs_reversed(nbr, sccid)

sccid = 0
print(f"topsort: {topsort}")
for vertex in topsort[::-1]:

    if visited_reversed[vertex] == -1:
        print(vertex)
        sccid += 1
        dfs_reversed(vertex, sccid)
print(departure)
print(visited_reversed[1:])







