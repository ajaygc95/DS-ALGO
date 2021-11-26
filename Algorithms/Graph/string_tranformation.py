
from collections import deque

words = ["cat", "hat", "bad", "had",]
start = "bat"
stop = "had"

aux = {}
input = words + ["bat"]

print(input)
for item in input:

    for i in range(len(item)):

        if item.replace(item[i],"*") not in aux:
            aux[item.replace(item[i],"*")] = [item]
        aux[item.replace(item[i],"*")].append(item)


final = {}
for item in input:
    final[item] = set()

for item in input:
    for i in range(len(item)):
        for j in aux[item.replace(item[i],"*")]:
            if j != item:
                final[item].add(j)


for item in final.items():
    print(item)

print()

visited = {item:False for item in input}
print(visited)
globalbox = [0]
parent = {}
def helper(start, end):

    if start == end:
        return start

    visited[start] = True

    q = deque([start])
    path = []
    while q:

        for _ in range(len(q)):
            new_node = q.popleft()


            for nbr in final[new_node]:
                print("hello")
                if not visited[nbr]:
                    parent[nbr] = new_node
                    q.append(nbr)
                    visited[nbr] = True


# print(min(globalbox))







