


adjlist = {
    0 : {1:1,2:4},
    1 : {0:1,2:4,3:2,4:7},
    2 : {0:4,1:4,3:3,4:5},
    3 : {1:2,2:3,4:4,5:6},
    4 : {1:7, 2:5, 3:4, 5:7},
    5 : {3:6, 4:7}
}



captured = [-1]*len(adjlist)
captured[0] = 1



def helper(start, end, input):


































# def overall(graph):

#     unvisited = {key:9999 for key in graph}
#     visited = {key:False for key in graph}

#     def helper(start, end, input):

#         unvisited[start] 

#         if visited[start] == False:
#             print("not visited", start)

#             visited[start] = True
            
#             for item in input[start]:
#                 helper(item,end,input)


#     helper(0, 0, graph)

#     print(unvisited)
#     print(visited)


# overall(graph)