'''
=========================================================================
============================= Kruskal's Algorithm =======================
=========================================================================

'''

edges = [(0,1,4), (1,2,3),(0,2,2)]
n = 3
connections = sorted(edges, key=lambda x: x[2]) # nlogn
parent = [x for x in range(n)]
size = [1]*n

def find(x):
    if x == parent[x]:
        return x
    rootx = find(parent[x])
    parent[x] = rootx
    return rootx
components = n
total_cost = 0
result = []
for u,v, weight in connections:
    findu = find(u)
    findv = find(v)

    if findu != findv:
        if size[findv] < size[findu]:
            parent[findv] = findu
            size[findu] += size[findv]
        else:
            parent[findu] = findv
            size[findv] += size[findu]

        components -= 1
        total_cost += weight
        result.append((u,v, weight))

if components == 1:  
    print (total_cost)
else:
    print(-1)

'''
Time Complexity --> sort(mlogm)  + union_find (O(n)) doing path compression
                --> n(logn) # if the graph is sparse 
Space Complexity -->
'''





















# from operator import itemgetter

# input = [(0,1,4), (1,2,3),(0,2,2)]
# n = 3
# connection = sorted(input, key=itemgetter(2))
# # connection = input
# print(connection)
# size = [1] * (n)
# parent = [x for x in range(n)]
# components = 3
# totalcost = 0
# result = []

# def find (x):
#     if x == parent[x]:
#         return x
#     x = parent[x]

# for u, v , weight in connection:
#     rootu = find(u)
#     rootv = find(v)

#     if rootu != rootv:
#         if size[rootu] <= size[rootv]:
#             parent[rootu] = rootv
#             size[rootv] += size[rootu]
#         else:
#             parent[rootv] = rootu
#             size[rootu] += size[rootv]
#         components -= 1
#         totalcost += weight
#         result.append((u,v))

# if components == 1:
#     print(f"totalcost: {totalcost} result: {result}")
# else: 
#     print("-1")



