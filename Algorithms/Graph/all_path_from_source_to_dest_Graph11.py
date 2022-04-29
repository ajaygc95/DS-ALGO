# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

#         n = len(graph)
#         def helper(node, slate):
#             #Base Case/ Leaf Node
#             if node == n-1:
#                 slate.append(node)
#                 result.append(slate[:])
#                 slate.pop()
#             #Recursive Case
#             slate.append(node) 
#             for nbr in graph[node]:
#                 helper(nbr, slate)
            
#             slate.pop()
            
#         # result = []
#         # helper(0, [])
#         # return result
    
#         # # T(N) --> O (2^(1/3)n) is greater than 1 
#         # #      --> Exponentianl 
#         # # S(N) --> Same as above

final = 5
 
def helper(somehting):
    final += 2

helper(2)
print(final)
