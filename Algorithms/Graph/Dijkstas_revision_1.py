import heapq
times = [[2,1,1],[2,3,1],[3,4,1]] 
n = 4
k = 2
adj = [[] for _ in range(n+1)]

for src, dest, weight in times:
    adj[src].append((dest,weight))

visited = [-1] * len(adj)
captured = [-1]* len(adj)

pq = [(k,0)]

totaldist = [0]
capturenum = [0]
def dijksta():

    while pq:
        node, dst = heapq.heappop(pq)
        print(node, dst)
        if captured[node] != -1:
            continue
        captured[node] = dst
        totaldist[0] = dst
        capturenum[0] += 1
        for nbr, w in adj[node]:
            if captured[nbr] == -1:
                heapq.heappush(pq, (nbr, w+dst))

dijksta()
if capturenum[0] == n:
    print(totaldist[0])
else:
    print("Come On")
