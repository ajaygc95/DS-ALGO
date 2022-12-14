class TreeNode:
    def __init__(self,val=0) -> None:
        self.val = val
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self) -> None:
        self.head = None

    def insert(self, item):
        new_node = TreeNode(item)
        if not self.head:
            self.head = new_node
            return 

        curr = self.head
        prev = None
        while curr:
            prev = curr
            if item < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if item > prev.val:
            prev.right = new_node
        else:
            prev.left = new_node
    
    def view(self, node):
        print(node.val)
        if node.left:
            self.view(node.left)
        if node.right:
            self.view(node.right)

    def succ(self, item):
        print(f"successsor of {item} is", end=" ")
        curr = self.head
        prev = None

        while curr:
            if curr.val == item:
                break
            if item < curr.val:
                prev = curr
                curr = curr.left
            else:
                curr = curr.right
 
        if curr.right:
            curr = curr.right
            while curr.left:
                curr = curr.left
            return curr.val
        else:
            if not prev:
                return f" No successor found '{item}' is the last value in the tree"
            return prev.val
        



tree = Tree()

tree.insert(20)
tree.insert(10)
tree.insert(15)
tree.insert(26)
tree.insert(24)
tree.insert(22)
tree.insert(23)
tree.insert(40)
tree.insert(29)
tree.insert(25)
tree.insert(35)
tree.insert(42)
tree.insert(48)


tree.view(tree.head)
print(tree.succ(42))


