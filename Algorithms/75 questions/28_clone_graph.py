adjList = [[2,4],[1,3],[2,4],[1,3]]

clone = {}
def dfs(node):
    if node in clone:
        return clone[node]
    copy = 
    for nbr in adjList[node]:
        dfs(nbr)
