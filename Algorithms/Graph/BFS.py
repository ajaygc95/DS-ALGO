from collections import deque
from queue import Queue


given = [(1,2),(2,3),(2,5),(3,4),(4,5)]
adj = {}


# def design(given):
#     if not given : return 

#     for source, dest in given:
#         if source not in adj:
#             adj[source] = [dest]
#         else:
#             adj[source].append(dest)

#         if dest not in adj:
#             adj[dest] = [source]
#         else:
#             adj[dest].append(source)


# design(given)


# visited = {key:0 for key in adj}
# parent = {}

# def BFS(start):
    
#     visited[start]= 1

#     q = deque()
#     q.append(start)

#     while q:
#         v = q.popleft()

#         for item in adj[v]:

#             if visited[item] == 0:
#                 visited[item] = 1
#                 parent[item] = v
#                 q.append(item)

# BFS(1)
# print("visited:", visited)
# print("parent:", parent)











def design(given):
    for source, dest in given:
        if not source in adj:
            adj[source] = [dest]
        else:
            adj[source].append(dest)

        if not dest in adj:
            adj[dest] = [source]
        else:
            adj[dest].append(source)

design(given)
len = len(adj)
visited = {}
parent ={}

for item in adj:
    visited[item] = 0

def bfs(node):
    
    visited[node] = 1
    q = deque()
    q.append(node)

    while q:
        v = q.popleft()
        for item in adj[v]:
            if visited[item] == 0:
                parent[item] = v
                visited[item] =1
                q.append(item)

bfs(1)
print(visited)
print(parent)