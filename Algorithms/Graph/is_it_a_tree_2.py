
from collections import deque
node_count = 4
edge_start = [0, 0, 0]
edge_end = [1, 2, 3]

adj_list = [[] for _ in range(node_count)]

for i in range(len(edge_start)):
    adj_list[edge_start[i]].append(edge_end[i])


visited = [-1] * len(adj_list)
parent = [-1] * len(adj_list)


def helper(root):

    visited[root] = 1
    
    for nbr in adj_list[root]:

        if visited[nbr] == -1:
            visited[nbr] = 1
            parent[nbr] = root

            if not helper(nbr):
                return False
        
        else:
            if nbr != parent[root]:
                return False
        
    return True


    visited[root] = 1
    parent[root] = None

    q = deque([root])

    while q:
        node = q.popleft()

        for v in adj_list[node]:

            if visited[v] == -1:
                visited[v] == 1
                q.append(v)
                parent[v] = node
            else:
                if v != parent[node]:
                    return False
    return True



count = 0
for i in range(len(visited)):
    
    if visited[i] == -1:
        count += 1

        if count > 1:
            print("False")
            break
        if helper(i):
            print(True)


































# input = [[0,1],[0,2],[0,3],[1,4]]

# adjlist = [[] for _ in range(node_count)]

# zipped = zip(edge_start,edge_end)

# for i,j in zip(edge_start, edge_end):
#     adjlist[i].append(j)
#     adjlist[j].append(i)
 

# # adjlist = {}

# # for src, dest in input:

# #     if src not in adjlist:
# #         adjlist[src] = [dest]
# #     else:
# #         adjlist[src].append(dest)
    
# #     if dest not in adjlist:
# #         adjlist[dest] = [src]
# #     else:
# #         adjlist[dest].append(src)

# visited = [-1]* (len(adjlist))
# parent = [-1]*(len(adjlist))
# print(adjlist)

# def helper(node):

#     visited[node] = 1

#     for nbr in adjlist[node]:
#         if visited[nbr] == -1:

#             parent[nbr] = node
#             visited[nbr] = 1
#             if helper(nbr):
#                 return True
#         else:
#             if parent[node] != nbr:
#                 return True
#     return False

# def overall():

#     for i in range(len(visited)):

#         if visited[i] == -1:
        
#             if helper(i):
#                 print("Truee cycle")
#                 return False
#             else:
#                 print("No Cycle")
#                 return True

#     return True

# overall()