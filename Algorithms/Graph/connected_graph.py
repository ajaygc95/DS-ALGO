
from collections import deque
input = [[0,1],[0,2],[0,3],[1,4]]
# 0 1
# 1 2
# 2 3
# 3 4
def overall(input):

    adjlist = {}

    for src, dest in input:

        if src not in adjlist:
            adjlist[src] = [dest]
        else:
            adjlist[src].append(dest)
        
        if dest not in adjlist:
            adjlist[dest] = [src]
        else:
            adjlist[dest].append(src)

    visited = [-1]* (len(adjlist))
    

    def helper(root):

        visited[root] = 1

        q = deque()
        q.append(root)

        while q:
            new_node = q.popleft()

            for nbr in adjlist[new_node]:

                if visited[nbr] == -1:
                    visited[nbr] = 1
                    q.append(nbr)

    count= 0
    for i in range(len(adjlist)):
        if visited[i] == -1:
            count += 1
            helper(i)
    return count

store = overall(input)
print(store)