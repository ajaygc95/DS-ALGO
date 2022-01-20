from time import time


n = 5
input = [(1,2),(2,3),(3,1),(3,4),(4,5),(5,4)]


def outer(input):

    adjlist = [[] for _ in range(n+1)]

    print(adjlist)

    for src, dest in input:
        adjlist[src].append(dest)

    visited = [-1]*len(adjlist)

    departure = [[]]*len(adjlist)

    timestamp = [0]

    def dfs(root):

        visited[root] = 1
        for nbr in adjlist[root]:

            print(nbr)
            if visited[nbr] == -1:
                dfs(nbr)
    
        departure[root] = timestamp[0]
        timestamp[0] += 1

    for v in range(1,len(visited)):
        if visited[v] == -1:
            dfs(v)

    print(departure)


outer(input)