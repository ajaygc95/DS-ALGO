import heapq

times = [[2,1,1],[2,3,1],[3,4,1]] 

n = 4
adjlist = [[] for _ in range(n+1)]

for src, dst, weight in times:
    adjlist[src].append((dst,weight))

captured = [-1] * len(adjlist)

print(adjlist)



