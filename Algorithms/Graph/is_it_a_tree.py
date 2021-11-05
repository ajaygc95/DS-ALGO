from collections import deque

input = [[0,1],[1,2],[2,3],[1,3],[1,4]]

visited = []
adjlist = {}
parent = []


def overall(input):
    n = len(input)+1
    adjlist = [[]  for _ in range(n)]

    for (src, dest) in input:
        adjlist[src].append(dest)
        adjlist[dest].append(src)

    visited = [-1] * n
    parent = [None] * n

    def bfs(node):
        visited[node] = 1
        q = deque()
        q.append(node)

        while q:
            node = q.popleft()
            for nbr in adjlist[node]:
                if visited[nbr] == -1:
                    visited[nbr] = 1
                    parent[nbr]  = node
                    q.append(nbr)
                else:
                    if nbr != parent[node]:
                        return True
        return False

    components = 0
    for v in range(n):
        if visited[v] == -1:
            components += 1
            if components > 1:
                return False
            if bfs(v):
                return False

    print(adjlist)
    print(visited)

    return True

store = overall(input)

print(store)
