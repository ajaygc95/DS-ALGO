
#input = n vertices with ids 1, 2, ...... n
#edges = an edge list


'''
adjlist = a 1d array of size n + 1

for (i,j) in  edges:
    adjlist[i].append(j)

visited = [-1] * len(adjlist)


def dfs(node):
    visited[node] = 1

    for nbr in adjlist[node]:
        if visited[nbr] == -1:
            dfs(nbr)


def outer ():
    components = 0
    for v in len(adjlist):
        if visited[v] == -1:
            components += 1

            if compnents > 1:
                return False
            else:
                dfs(v)
            
# since we started from dfs(1)
if v is not able to be visited :
    return counter example (1, v)
    1 being starting vertex 
    v which can't be reaced. 


'''


# adjlist_reversed = 1 d arry of len n+1

# build edges using orgiinal graph ( adjlist)
# =====================================================
# ======= below is for reversing the graph ============
# =====================================================

'''
for v in 1 to n:
    for each neighbor in adjlist[v]:
        adjlistr[nbr] .append(v)

'''

# do same thing for ajdlist_reversed