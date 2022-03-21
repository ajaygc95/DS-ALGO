import heapq
from math import dist
times = [[2,1,1],[2,3,1],[3,4,1]] 

n = 4
adjlist = [[] for _ in range(n+1)]

for src, dst, weight in times:
    adjlist[src].append((dst,weight))

captured = [-1] * len(adjlist)

print(adjlist)


# pq = [(0,2)]
# numcaptured = 0
# lastdist = 0
# while pq:
#     (dst, node) = heapq.heappop(pq)
#     print(dst,node)

#     if captured[node] != -1:
#         continue

#     captured[node] = dst
#     numcaptured += 1
#     lastdist = dst
#     for nbr, w in adjlist[node]:
#         if captured[nbr] == -1:
#             heapq.heappush(pq, (w+captured[node], nbr))

# if numcaptured == n:
#     print(lastdist)

