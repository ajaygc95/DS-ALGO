def strongly_connected_graph():
    # edges = [[1,2],[2,3],[3,1],[1,4],[3,4]]
    edges = [[1,2],[2,4],[2,3],[3,1],[4,2]]
    n = 4

    adjlist = [[]for _ in range(n+1)]

    for src, dst in edges:
        adjlist[src].append(dst)

    visited = [-1]*(n+1)
    arrival = [-1]*(n+1)
    departure = [-1]*(n+1)
    lowestarr = [-1]*(n+1)
    timestamp = [0]
    res = []
    def dfs(node):
        visited[node] = 1
        timestamp[0] += 1
        arrival[node] = timestamp[0]
        lowestarr[node] = timestamp[0]
        
        for nbr in adjlist[node]:
            if visited[nbr] == -1:
                lowestarr[node] = min(lowestarr[node], dfs(nbr))
            else:
                if arrival[nbr] < lowestarr[node]:
                    lowestarr[node] = min(arrival[nbr], lowestarr[node])

        if lowestarr[node] == arrival[node] and node != 1: # 1 is root here 
            res.append((node,1))

        return lowestarr[node]

    dfs(1)

    for v in range(1, n):
        if visited[v] == -1:
            return (n,1)

    return True if len(res) == 0 else res[0]

result = strongly_connected_graph()
print(result)

    



