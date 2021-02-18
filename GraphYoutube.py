__author__ = "Ajay GC"


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbour = {}
        self.distance = 9999
        self.visited = False

    def add_neighbor(self, nbr, weight):
        self.neighbour[nbr] = weight

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,key):

        newvertex = Vertex(key)
        self.vertices[key] = newvertex

    def add_edge(self,first,second, weight):
        if first in self.vertices and second in self.vertices:
            for key, value in self.vertices.items():
                if key == first:
                    value.add_neighbor(second, weight)
                if key == second:
                    value.add_neighbor(first,weight)
            return True
        else:
            return False

    def BFS(self,start):
        letters = []
        start.distance = 0
        start.visited = True

        for item in start.neighbour:
            self.vertices[item].distance = start.distance +1
            letters.append(item)

        while len(letters)>0:
            new_item = letters.pop(0)
            node_new_item = self.vertices[new_item]
            node_new_item.visited = True


            for third_item in node_new_item.neighbour:
                node_third_item = self.vertices(node_third_item)
                letters.append(third_item)
                if not node_third_item:
                    letters.append(third_item)
                    if node_third_item > node_new_item +1:
                        node_third_item = node_new_item +1


    def view(self):
        for key in self.vertices.keys():
            print(self.vertices[key].neighbour,self.vertices[key].distance)

vertex = Vertex('A')
a =  Graph()
for i in range(ord('A'), ord('K')):
    a.add_vertex(chr(i))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

count = 1
for edge in edges:
    a.add_edge(edge[:1], edge[1:],count)
    count += 1

a.BFS(vertex)
a.view()