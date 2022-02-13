'''
===========================================================
================= Dijkstra's Algorithm ====================
===========================================================

'''


import heapq


times = [[2,1,1],[2,3,1],[3,4,1]] 
n = 4
k = 2

adj_list = [[] for _ in range(n+1)]

for src, dest, weight in times:
    adj_list[src].append((dest, weight))

captured = [-1] * (len(adj_list))
lastdist = 0
numcaptured = 0


q = [(0,k)]

while q :
    (dist, node) = heapq.heappop(q)

    if captured[node] != -1:
        continue

    captured[node] = dist
    lastdist = dist
    numcaptured += 1


    for (nbr, weight) in adj_list[node]:
        if captured[nbr] == -1:
            heapq.heappush(q, (weight+captured[node], nbr))
    

if numcaptured == n:
    print(lastdist)
else:
    print("-1")

# print(adj_list)





# import heapq
# from time import time


# times = [[2,1,1],[2,3,1],[3,4,1]] 
# n = 4
# k = 2


# def helper(times, n, k):
#     adjlist = [ [] for _ in range(n+1)]


#     for src, dest, w in times:
#         adjlist[src].append((dest, w))


#     captured = [-1]*(n+1)
#     lastdist = 0
#     numcaptured = 0
#     q = [(0,k)]

#     while q:
#         (dist, node) = heapq.heappop(q)

#         if captured[node] != -1:
#             continue

#         captured[node] = dist
#         lastdist = dist
#         numcaptured += 1
#         for nbr, weight in adjlist[node]:
#             if captured[nbr] == -1:
#                 heapq.heappush(q,(captured[node] + weight,nbr))
            
        
#     if numcaptured == n:
#         return lastdist
#     else:
#         return -1

        
# store = helper(times,n,k)
# print(store)


























# # def overall(graph):

# #     unvisited = {key:9999 for key in graph}
# #     visited = {key:False for key in graph}

# #     def helper(start, end, input):

#         unvisited[start] 

#         if visited[start] == False:
#             print("not visited", start)

#             visited[start] = True
            
#             for item in input[start]:
#                 helper(item,end,input)


#     helper(0, 0, graph)

#     print(unvisited)
#     print(visited)


# overall(graph)