
from collections import deque
from typing import Pattern

prerequisite = [[1, 0], [2, 0], [3, 1], [3, 2]]

n = 4

adjlist = [[] for _ in range(n)]


for (i , j) in prerequisite:
    adjlist[i].append(j)
    adjlist[j].append(i)




visited = [-1]*(n)
departure = [-1]*(n)
topsort = []

def helper(root):
    print(root)
    visited[root] = 1

    for item in adjlist[root]:
        print(item)
        if visited[item] == -1:
            if not helper(item):
                return False
        else:
            if departure[item] == -1:
                return False
    departure[root] == 1
    topsort.append(root)


for i in range(n):
    if visited[i] == 0:
        helper(i)

print(topsort)

























# for item in adjlist:
#     print(item)


# visited = []
# parent = {}
# course = []
# def helper(root):
#     start = root
#     visited.append(root)
#     q = deque()
#     q.append(root)
    
#     while q:

#         print(q)
#         node = q.popleft()

#         for v in adjlist[node]:
            
#             if v not in visited:
#                 course.append(v)
#                 visited.append(v)
#                 q.append(v)
#                 parent[v] = node
#             else:
#                 return False
#     course.append(root)
# helper(0)
# print(course)


        



