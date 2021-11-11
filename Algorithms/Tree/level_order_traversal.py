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




 

















def overall(root):
    result = []
    def bfs(root):
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    bfs(root)
    return result


store = overall(tree)
print(store)