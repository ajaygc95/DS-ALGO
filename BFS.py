__author__ = "Ajay GC"

''' Breadth First Search '''

from graphDS import Graph, Vertex
from Queue import  Queue


''' Distance 
    Parent 
    visited
'''

def BFS(start):
    all_items = []
    parent = None
    visited = False
    q = Queue()
    q.enqueue(start)

    for nbr in







