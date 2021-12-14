

n =  5

connections = [

[0, 1],

[0, 2],

[0, 4],

[1, 2],

[1, 3]

]

def find_critical_connections(number_of_servers, connections):
    # Write your code here
    # no_criticals = [[-1,-1]]
    n = number_of_servers
    
    # if n < 2 or len(connections) < 1: return no_criticals
    
    adj = [[] for _ in range(n)]


    for i, j in connections:
        adj[i].append(j)
        adj[j].append(i)
        
    visited = [-1] * len(adj)
    parent = {}
    arrival = [-1] * n
    lowestarr = [-1] * n
    timestamp = [0]
    criticals = []
    parent[0] = None

    def dfs(node):

        visited[node] = True

        arrival[node] = timestamp[0]
        timestamp[0] += 1
        lowestarr[node] = arrival[node]

        for nbr in adj[node]:
            if visited[nbr] == -1:
                parent[nbr] = node
                lowestarr[node] = min(lowestarr[node], dfs(nbr))
            elif nbr != parent[node]:
                lowestarr[node] = min(lowestarr[node], lowestarr[nbr])
                
        if lowestarr[node] == arrival[node] and arrival[node] != 0:
            criticals.append([node, parent[node]])
            
        return lowestarr[node]
        
    dfs(0)
    
    return criticals 
    # if criticals else no_criticals



store = find_critical_connections(n, connections)
print(store)
# from collections import deque

# adj_list = [[] for _ in range(n)]


# for i, j in connections:
#     adj_list[i].append(j)
#     adj_list[j].append(i)



# visited = [-1] * len(adj_list)



# arrival = [-1] * len(adj_list)
# departure = [-1] * len(adj_list)

# lowestarr = [-1] * len(adj_list)

# timestamp = [0]

# criticals = []

# parent = [-1] * len(adj_list)

# def dfs(node):
#     visited[node] = True
#     timestamp[0] += 1
#     arrival[node] = timestamp[0]
#     lowestarr[node] = arrival[node]
    
#     for nbr in adj_list[node]:
#         if not visited[nbr]:
#             parent[nbr] = node
#             nbr_lowest_arr = dfs(nbr)
#             lowestarr[node] = min(lowestarr[node], nbr_lowest_arr)
#         elif nbr != parent[node]:
#             lowestarr[node] = min(lowestarr[node], arrival[nbr])
            
#     if lowestarr[node] == arrival[node] and arrival[node] != 0:
#         criticals.append([node, parent[node]])
        
#     return lowestarr[node]


# dfs(0)

# print(criticals)