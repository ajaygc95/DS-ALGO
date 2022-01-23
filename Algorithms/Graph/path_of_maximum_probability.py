'''
         0
    0.5 / \ 0.2
       /   \ 
      1 --- 2
        0.5
=========================================================
================= Problem Reduction =====================
=========================================================

'''

import heapq
from logging import captureWarnings
import math


n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0 
end = 2


# Build the Graph

def solve_the_problem():
    adjlist = [[] for _ in range(n)]

    for i in range(len(edges)):

        (src,dst) = edges[i]
        adjlist[src].append((dst, -math.log(succProb[i])))
        adjlist[dst].append((src, -math.log(succProb[i])))

    captured = [-1]*(n)
    q = [(0, start)]

    while q:
        (dist, node) = heapq.heappop(q)

        if captured[node] != -1:
            continue

        captured[node] = dist

        print(captured)
        for nbr, weight in adjlist[node]:
            if captured[nbr] == -1:
                heapq.heappush(q, (weight + captured[node], nbr))

    if captured[end] == -1:
        return 0

    else:
        return math.exp(-captured[end])

store = solve_the_problem()
print(store)