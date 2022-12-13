#########################################################################
############################## Two Passes ###############################
#########################################################################

edges = [[1,2],[2,3],[3,1],[1,4],[3,4]]
n = 4
adjlist = [[] for _ in range(n+1)]

for src, dst in edges:
    adjlist[src].append(dst)

visited = [-1] * (n+1)

def dfs(node):
    visited[node] = 1
    for nbr in adjlist[node]:
        if visited[nbr] == -1:
            dfs(nbr)

components = 0

for v in range(1,n):
    if visited[v] == -1:
        components += 1
        if components <= 1:
            dfs(v)
        else:
            print(1, v)
            break

adjlist_reversed = [[] for _ in range(n+1)]

for vertex in range(1, n):

    for nbr in adjlist[vertex]:
        adjlist_reversed[nbr].append(vertex)

visited_reversed = [-1]*(n+1)

print(adjlist)
print(adjlist_reversed)

def dfsr(node):
    visited_reversed[node]= 1

    for nbr in adjlist_reversed[node]:
        if visited_reversed[nbr] == -1:
            dfs(nbr)

components = 0
for v in range(1, n):
    if visited_reversed[v] == -1:
        components += 1
        if components == 2:
            print(1, v)
            break
        dfsr(v)



        





