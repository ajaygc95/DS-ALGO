
from collections import deque
n =4
a = [1,1,3]
b =[0,2,1]


adj_list = [[] for _ in range(n)]

for i in range(len(a)):
    adj_list[a[i]].append(b[i])
    # adj_list[b[i]].append(a[i])

visited = [-1] * len(adj_list)

departure = [-1] * len(adj_list)
arrival = [-1] * len(adj_list)
timestamp = [0]

def helper(root):
    arrival[root] = timestamp[0]
    timestamp[0] += 1
    visited[root] = 1

    for nbr in adj_list[root]:

        if visited[nbr] == -1:
            if not helper(nbr):
                return False

        else:
            if root != visited[nbr]:
                return False

    departure[root] = timestamp[0]
    timestamp[0] += 1

    return True


for i in range(len(visited)):

    if visited[i] == -1:
        helper(i)