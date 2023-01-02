import heapq

# times = [[2,1,1],[2,3,1],[3,4,1]] 
times = [[1,2,2],[1,3,5],[2,5,2],[5,4,2],[3,4,6]]
n = 5
adjlist = [[] for _ in range(n+1)]
dsetination = 4
for src, dst, weight in times:
    adjlist[src].append((dst,weight))

captured = [-1] * (n+1)

pq = [(0, 2)]
distance = [-1]*(n+1)
while pq:
    weight, node = heapq.heappop(pq)

    if captured[node] != -1:
        continue
    
    captured[node] = 1
    distance[node] = weight

    for nbr, wt in adjlist[node]:
        heapq.heappush(pq, (wt+distance[node], nbr))

print(distance[4])
'''
T(n) --> mlogm 
'''







