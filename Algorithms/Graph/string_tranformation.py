
from collections import deque

words = ["aaa","kkk"]
start = "baa"
stop = "aab"

def string_transformation(words, start, stop):
    if start == stop:
        return -1
    
    input = words + [start]
    
    if stop not in words:
        input.append(stop)
    
    print(input)
    
    aux = {}
    
    for item in input:
    
        for i in range(len(item)):
            pattern = item[:i] +"*" + item[i+1:]

            if pattern not in aux:
                aux[pattern] = [item]
            if item not in aux[pattern]:
                aux[pattern].append(item)


    
    final = {}
    for item in input:
        final[item] = set()
    
    for item in input:
        for i in range(len(item)):

            pattern = item[:i] +"*" + item[i+1:]
            for j in aux[pattern]:
                if j != item:
                    final[item].add(j)
                   
    # print("===================")
    # for item in final.items():
    #     print(item)
    visited = {item:False for item in input}
    

    parent = {}
    
    visited[start] = True
    
    q = deque([start])
    
    while q:
    
        for _ in range(len(q)):
            new_node = q.popleft()
    
            for nbr in final[new_node]:
                
                if not visited[nbr]:
                    parent[nbr] = new_node
                    q.append(nbr)
                    visited[nbr] = True
    
    new_path = []

    parent[start] = None
    node = stop
    prev = None
    while node is not None:
        new_path.append(node)
        prev = node
        node = parent[node]
    print(prev)
    return new_path[::-1]
    



store = string_transformation(words, start, stop)

print(store)

# aux = {}


# input = words + ["bat"]


# print(input)
# for item in input:

#     for i in range(len(item)):

#         if item.replace(item[i],"*") not in aux:
#             aux[item.replace(item[i],"*")] = [item]
#         aux[item.replace(item[i],"*")].append(item)


# final = {}
# for item in input:
#     final[item] = set()

# for item in input:
#     for i in range(len(item)):
#         for j in aux[item.replace(item[i],"*")]:
#             if j != item:
#                 final[item].add(j)


# visited = {item:False for item in input}

# parent = {}

# visited[start] = True

# q = deque([start])

# while q:

#     for _ in range(len(q)):
#         new_node = q.popleft()

#         for nbr in final[new_node]:
#             if not visited[nbr]:
#                 parent[nbr] = new_node
#                 q.append(nbr)
#                 visited[nbr] = True

# new_path = []

# parent[start] = None
# node = stop

# while node is not None:
#     new_path.append(node)
#     node = parent[node]

# print(new_path)

# print(new_path[::-1])


