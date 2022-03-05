'''
=========================================================================
============================= Kruskal's Algorithm =======================
=========================================================================

'''
from operator import itemgetter

input = [(0,1,4), (1,2,3),(0,2,2)]
n = 3
connection = sorted(input, key=itemgetter(2))

size = [1] * (n)
parent = [x for x in range(n)]
components = 3
totalcost = 0
result = []

def find (x):
    if x == parent[x]:
        return x
    x = parent[x]

for u, v , weight in connection:
    rootu = find(u)
    rootv = find(v)

    if rootu != rootv:
        if size[rootu] <= size[rootv]:
            parent[rootu] = rootv
            size[rootv] += size[rootu]
        else:
            parent[rootv] = rootu
            size[rootu] += size[rootv]
        components -= 1
        totalcost += weight
        result.append((u,v))

if components == 1:
    print(f"totalcost: {totalcost} result: {result}")
else: 
    print("-1")

