#graph 

'''
Vetex = Points circles
edge are lines
Weight = value of the lines lets say 5

G = (V,E)


Needed function 

class Graph()--> To store graph and weight 
addvertex(vert) --> Add Vertex  lets sas addvertex (A)
addEdgge() --> Add Edges   connects(A -> B )
addEdge() --> add Edges with weight (A -> B , 5)
getVertex(key)
getVertices () --> List of all the vertices. 

getE
'''


class Graph:
    def __init__(self) -> None:
        self.id = id # Vertex
        self.adj = {} # value and weight. 

    def addvertex()