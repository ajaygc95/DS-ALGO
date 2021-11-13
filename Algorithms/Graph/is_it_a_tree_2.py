
from collections import deque
node_count = 4
edge_start = [0, 0, 0]
edge_end = [1, 2, 3]

input = [[0,1],[0,2],[0,3],[1,4]]

adjlist = [[] for _ in range(node_count)]

zipped = zip(edge_start,edge_end)

for i,j in zip(edge_start, edge_end):
    adjlist[i].append(j)
    adjlist[j].append(i)
 

# adjlist = {}

# for src, dest in input:

#     if src not in adjlist:
#         adjlist[src] = [dest]
#     else:
#         adjlist[src].append(dest)
    
#     if dest not in adjlist:
#         adjlist[dest] = [src]
#     else:
#         adjlist[dest].append(src)

visited = [-1]* (len(adjlist))
parent = [-1]*(len(adjlist))
print(adjlist)

def helper(node):

    visited[node] = 1

    for nbr in adjlist[node]:
        if visited[nbr] == -1:

            parent[nbr] = node
            visited[nbr] = 1
            if helper(nbr):
                return True
        else:
            if parent[node] != nbr:
                return True
    return False

def overall():

    for i in range(len(visited)):

        if visited[i] == -1:
        
            if helper(i):
                print("Truee cycle")
                return False
            else:
                print("No Cycle")
                return True

    return True

overall()