# class Graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.idict = {}

#         for key, pair in edges:
#             if key in self.idict:
#                 self.idict[key].append(pair)
#             if key not in self.idict:
#                 self.idict[key] = [pair]
#         print(self.idict)
#         print("========================================================")
        
#     def find_path(self,start,end, path=[]):

#         path = path + [start]
#         if start == end:
#             return [path]
#         if start not in self.idict:
#             return []
#         paths = []
#         for node in self.idict[start]:
#             if node not in path:
#                 print(node)
#                 new_paths = self.find_path(node,end,path)
#                 for p in new_paths:
#                     paths.append(p)
#         # print(path)
#         return paths


class Graph:
    def __init__(self,data) -> None:
        self.data = data
        self.storage = {}
        for key, value in self.data:
            if key not in self.storage:
                self.storage[key] = [value]          
            elif  key in self.storage:
                self.storage[key].append(value)  
    
    def find_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path
        


if __name__ == "__main__":
    routes = [
        ('mumbai','dubai'),
        ('mumbai','paris'),
        ('paris','dubai'),
        ('paris','new york'),
        ('dubai','paris'),
        ('dubai','new york'),
        ('new york','toronto')
    ]

    gh = Graph(routes)
    # final_path = gh.find_path('mumbai','toronto')

    # print(final_path)
    