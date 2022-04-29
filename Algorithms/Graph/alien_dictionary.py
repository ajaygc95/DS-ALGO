words = ["wrt", "wrf", "er", "ett", "rftt"]

adj = {c:set() for w in words for c in w}

for i in range(len(words)-1):
    w1 , w2 =  words[i], words[i+1]

    to_go = min(len(w1), len(w2))

    for i in range(to_go):
        if w1[i] != w2[i]:
            adj[w1[i]].add(w2[i])
            break

visited = {}
timestamp = [0]
topsort = []

def dfs(node):
    visited[node] = True

    for nbr in adj[node]:
        if nbr not in visited:
            visited[nbr] = True
            dfs(nbr)

    topsort.append(node)



dfs("w")

print(adj)
print(''.join(topsort[::-1]))