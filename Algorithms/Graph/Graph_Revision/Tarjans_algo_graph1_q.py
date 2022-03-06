n = 5
arrival = [None] * n
timestamp = [0]
lowestarr = [-1]*n

def dfs(node):

    arrival[node] = timestamp[0]

    for nbr in adjlist[node]:
        if nbr not in visited:
            lowestarr[node] = min(loswestarr[node], dfs(nbr))
        else:
            if parent[node] != nbr:
                lowestarr[]