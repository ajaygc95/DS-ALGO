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


from collections import deque
# from typing import Pattern

# prerequisite = [[1, 0], [2, 0], [3, 1], [3, 2]]

# n = 4
# adjlist = [[] for _ in range(n)]

# for (i , j) in prerequisite:
#     adjlist[i].append(j)

# visited = [-1]*n
# arrival = [-1]*n
# departure = [-1]*n
# timestamp = [0]
# topsort = []


# def helper(root):

#     arrival[root] = timestamp[0]
#     # timestamp[0] += 1

#     visited[root] = 1

#     for item in adjlist[root]:
#         # print(item)
#         if visited[item] == -1:
#             if helper(item):
#                 return True
#         else:
#             if departure[item] == -1:
#                 return True
    
#     departure[root] = timestamp[0]
#     # print(timestamp)
#     print("dep", departure)
#     timestamp[0] += 1

#     topsort.append(root)

#     return False

# for i in range(n):
#     if visited[i] == -1:
#         if helper(i):
#             print("not found")

# print(topsort[::-1])

























# # for item in adjlist:
# #     print(item)


# # visited = []
# # parent = {}
# # course = []
# # def helper(root):
# #     start = root
# #     visited.append(root)
# #     q = deque()
# #     q.append(root)
    
# #     while q:

# #         print(q)
# #         node = q.popleft()

# #         for v in adjlist[node]:
            
# #             if v not in visited:
# #                 course.append(v)
# #                 visited.append(v)
# #                 q.append(v)
# #                 parent[v] = node
# #             else:
# #                 return False
# #     course.append(root)
# # helper(0)
# # print(course)


        



