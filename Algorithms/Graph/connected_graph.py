
from collections import deque
'''
=========================================
=========== Tarjan's Algorithm ==========
=========================================

'''

input = [[0,1],[0,2],[0,3],[1,4]]
iinput = [

[0, 1],

[0, 2],

[0, 4],

[1, 2],

[1, 3]

]
# 0 1
# 1 2
# 2 3
# 3 4

def overall(input):

    adj_list = [[] for _ in range(len(input))]
    print(adj_list)

    for i,j in input:
        adj_list[i].append(j)
        adj_list[j].append(i)
    
    print(adj_list)

    visited = [-1]* len(adj_list)
    arrival = [-1] * len(adj_list)
    departure = [-1] * len(adj_list)

    timestamp = [0]
    parent = {}
    lowestarr = [-1] * len(adj_list)
    result = []
    parent[0] = None
    def helper(root):

        arrival[root] = timestamp[0]
        timestamp[0] += 1
        visited[root] = 1
        lowestarr[root] = arrival[root]

        for nbr in adj_list[root]:
            if visited[nbr] == -1:
                parent[nbr] = root
                lowestarr[root] = min(helper(nbr), lowestarr[root])
            else:
                if nbr != parent[root] :

                    lowestarr[root] = min(arrival[nbr], lowestarr[root])

        if lowestarr[root] == arrival[root] and root != 0:
            result.append((root, parent[root]))

        return lowestarr[root]
    
    helper(0)

    return result
                     
store = overall(iinput)
print(store)