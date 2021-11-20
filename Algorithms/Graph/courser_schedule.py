from collections import deque

input = [[1, 0], [2, 0], [3, 1], [3, 2]]


adjlist = [[] for _ in range(len(input))]
print(adjlist)

for (i,j) in input:
    adjlist[i].append(j)
    adjlist[j].append(i)


visited = [-1]*len(adjlist)+1
parent = []
def helper(node):

    visited[node] = 1
    q = deque([node])

    while q:
        new_node = q.popleft()

        for item in adjlist[new_node]:

            if visited[item] == -1:
                visited[item] == 1
                parent[item] == new_node
                q.append(item)
            else:
                if item != parent[node]:
                    return False


for v in visited:
    count = 0
    if visited[v] == -1:
        count += 1
        if count <= 1:
            helper(v)







    


print(adjlist)
