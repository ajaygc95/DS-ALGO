from collections import deque 


class Node:
    def __init__(self, val ) -> None:
        self.val = val
        self.right = None
        self.left = None

    def insert(self, item):
        new_node = Node(item)
        if self.val is None:
            self.val = new_node
            return
        
        if item < self.val:
            if self.left:
                self.left.insert(item)
            else:
                self.left = new_node

        else:
            if self.right:
                self.right.insert(item)
            else:
                self.right = new_node

    def in_order(self):
        elements = []
        print(self.val)
        if self.left:
            elements += self.left.in_order()

        elements.append(self.val)
        if self.right:
            elements += self.right.in_order()
        return(elements)



input = [5,4,7,1,11,12,15,3]

        

tree = Node(input[0])

for item in range(1,len(input)):
    tree.insert(input[item])

def BFS(tree):
    if not tree:
        return "This is it"

    q = deque([tree])

    result = []

    while q:
        len_q = len(q)  
        temp = []
        for _ in range(0,len_q):

            node = q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(temp)
    
    return result
    

def DFS(tree):

    if not tree.left and not tree.right:
        return

    if tree.left:
        DFS(tree.left)
    if tree.right:
        DFS(tree.right)



def overall(tree):
    if not tree:
        return []

    DFS(tree)

# to_print = BFS(tree)
to_print = DFS(tree)
print(to_print)










