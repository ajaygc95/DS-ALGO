from collections import deque

input = [(0, 2), (1, 2), (1, 4), (2, 3) ,(3, 4)]

adj_list = [[] for _ in range(len(input))]

for i,j in input:
    adj_list[i].append(j)
    adj_list[j].append(i)


visited = [-1] * len(adj_list)
parent = [-1]* len(adj_list)

distance = {}

def helper(root):
    distance[root] = 0
    visited[root] = 1
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()

        for nbr in adj_list[node]:

            if visited[nbr] == -1:
                visited[nbr] = 1
                parent[nbr] = node
                distance[nbr] = distance[node] + 1
                q.append(nbr)
            else:
                if distance[nbr] == distance[node]:
                    return False
    return True


# for i in range(len(visited)):

#     if visited[i] == -1:
#         print(helper(i))

