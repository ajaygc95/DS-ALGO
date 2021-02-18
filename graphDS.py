__author__ = "Ajay GC"


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.visited = False
        self.distance = 9999


    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t],weight)

    def getvertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return  iter(self.vertList.values())

graph = Graph()
graph.addVertex('A')
graph.getVertex('A')
graph.addEdge('A','B',5)
graph.addEdge('A','C',10)
toprint = graph.getvertices()
print(toprint)
