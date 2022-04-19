from collections import deque
def outer():
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
        
    n = numCourses
    
    adjlist = [[] for i in range(n)]
    
    for i , j in prerequisites:
        adjlist[i].append(j)
    
    visited = [-1]*n
    parent = {}
    parent[0] = None

    def bfs(node):
        visited[node]= 1
        q = deque()
        q.append(node)

        while q:
            v = q.popleft

            for nbr in adjlist[node]:
                if visited[node] == -1:
                    visited[node] = 1
                    q.append(nbr)
                else:
                    if parent[node] != nbr:
    #                     return False
    #     return True
    # return bfs(0)
    

print(outer)