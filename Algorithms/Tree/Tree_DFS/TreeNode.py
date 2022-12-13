import collections
class TreeNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.left = None
        self.right = None
    

    def insert(self,key):   
        print("Inserting:", key)
        
        curr = self
        prev = None
        while curr:
            if key == curr.val:
                return
            elif key < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
    
        new_node = TreeNode(key)

        if key < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node


    def view(self, node, res):
        res.append(node.val)
        if node.left:
            self.view(node.left,res)
        if node.right:
            self.view(node.right,res)
        return res

    def tree_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        
        return curr.val
    
    def max_tree(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val
    
    def delete(self, key):
        print("Delete Started .....")

        curr = self
        while curr:
            if key == curr.val:
                break
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        prev = curr
        succ = curr
        if curr.left and curr.right:
   
            while succ.left:
                prev = succ
                succ = succ.left

        curr.val = succ.val
        if succ is prev.left:
            prev.left = succ.right
        else: # succ is right
            prev.right = succ.right

        return self
        
        
def succesor(root, node):
    if not root:
        return 
    curr = root
    prev = None

    while curr:
        print(curr.val)
        if curr == node:
            break

        if node.val < curr.val:
            print("left", curr.val)
            prev = curr
            curr = curr.left
        else:
            curr = curr.right
    print("after while loop", curr.val, prev.val)
    if curr.right:
        while curr.right:
            curr = curr.right
        return curr.val
    
    return prev.val


def predecessor(root, node):
    print("pred")
    if not root:
        return 
    curr = root
    ancester = None
    while curr:
        print(curr.val)
        if curr == node:
            break
        if node.val < curr.val:
            curr = curr.left
        else:
            print("last right", curr.val)
            ancester = curr
            curr = curr.right
    if curr.left:
        while curr.left:
            curr = curr.left
        return curr.val
    
    return ancester.val
     
tree = TreeNode(17)

nums = [44, 17, 88, 8, 32, 65, 97, 28, 54, 82, 93, 29, 76, 68, 80]

for item in nums:
    tree.insert(item)
# result = tree.view(tree, [])
# print(result)
# delete_tree = tree.delete(8)
# deleted_result = tree.view(delete_tree, [])
# print(deleted_result)
# print(tree.tree_min())
# print(tree.max_tree())
# two_two = tree.right.right.left.right.right
# succ = succesor(tree, two_two)
# pred = predecessor(tree, two_two)

# print(f"pred: {pred} succ: {succ}")
print("printing Tree ")
print("===============================")
def bfs(tree):
    queue = collections.deque([tree])
    res = []
    while queue:
        len_q = len(queue)
        temp = []
        for _ in range(len_q):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(temp)
    return res
result = bfs(tree)
for item in result:
    print(item)
    

