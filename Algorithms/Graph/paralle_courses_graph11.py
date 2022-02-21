# from os import times

# n = 3
# relations = [[1,3],[2,3]]

# def outer(n, relations):

#     adjlist = [[] for _ in range(n+1)]

#     for src, dst in relations:
#         adjlist[src].append(dst)

#     visited = [-1]*len(adjlist)
#     departure = [-1]*len(adjlist)
#     timestamp = [0]
#     topsort = []


#     def helper(node):
#         visited[node] = 1

#         for nbr in adjlist[node]:
#             if visited[nbr] == -1:
#                 if helper(nbr):
#                     return True
#             elif departure[nbr] == -1:
#                 return True
        
#         topsort.append(node)
#         departure[node] = timestamp[0]
#         timestamp[0] += 1

#         return False



#     for v in range(1, len(adjlist)):
#         if visited[v] == -1:
#             if helper(v):
#                 return -1
#     topsort.reverse()

#     dptable = [1]*(n+1)

#     for curr in topsort:
#         for nbr in adjlist[curr]:
#             dptable[nbr] = max(dptable[nbr], 1 + dptable[curr])
    
#     return dptable


# store = outer ( n, relations)
# print(store)

# result = {"A":10}
# result = ([0], 2 ,3)

result = 2

def outer():

    def helper(someting):
        print(result)

    store = helper(2)

outer()

# print(result)
