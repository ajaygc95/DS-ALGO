__author__ = "Ajay GC"

class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbour = {}
        self.visited = False

    def add_neighbour(self, nbr, weight=0):
        self.neighbour[nbr] = weight

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,item):
        vertex = Vertex(item)
        self.vertices[item] = vertex

    def add_edge(self, start , end , weight):
        if start not in self.vertices:
            self.add_vertex(start)
        if end not in self.vertices:
            self.add_vertex(end)
        self.vertices[start].add_neighbour(end, weight)

    def view(self):
        for key, value in self.vertices.items():
            print(key, value.neighbour)

    # def DFS(self, start, end , path = []):
    #     path += [start]
    #     if start not in self.vertices:
    #         return []
    #     if start == end:
    #         return path
    #     for item in self.vertices[start].neighbour:
    #         if item not in path:
    #             self.DFS(item,end,path)
    #     return path
    #
    # def DFS_UTIL(self):
    #     visited =

    def _DFS(self,start, visited):
        visited.append(start)

        for neighbour in self.vertices[start].neighbour:
            if neighbour not in visited:
                self._DFS(neighbour,visited)

    def DFS(self):
        visited = []
        for vertex in self.vertices:
            if vertex not in visited:
                self._DFS(vertex,visited)

        return visited





graphD = Graph()
graphD.add_vertex('A')
graphD.add_edge('A','B',5)
graphD.add_edge('B','C',8)
graphD.add_edge('C','J',8)
graphD.add_edge('J','K',8)
graphD.add_edge('C','B',8)
graphD.add_edge('A','F',3)


toprint = graphD.DFS()
print(toprint)