# Build The Graph
'''
-- Implicit representation of edges
(No AdjList, n = infinity)

'''

import collections

def getnbr(a,b):
    list = [(a+1,b+2), (a+2,b+1),(a+2,b-1),(a+1,b-2), (a-1,b-2),(a-2,b-1), (a-2,b-1), (a-2,b+1),(a-1, b+2)]

    return list #list of all the nbr

visited = {}
visited[(0,0)] = 0 # Shortest path form (0,0) to that vertex


def helper(root,x,y):

    #Edge case

    if (x,y) == (0,0):
        return None
    
    q = collections.deque()
    q.push((0,0))
    while q :
        node = q.popleft()
        # (nodeX, nodeY)

        for nbr in getnbr(nbr):
            if nbr not in visited:
                visited[nbr] = 1 + visited[node]
                q.push(nbr)

                if nbr == (x,y):
                    return visited[(x,y)]

# def outerloop(input): #not needed.