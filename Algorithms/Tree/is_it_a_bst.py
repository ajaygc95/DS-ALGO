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


tree = Node(200)
tree.right = Node(300)
tree.left = Node(100)

def is_it_a_bst(root, floor, ceiling):

    if not root:
        return True

    if floor <= root.val <= ceiling:
        return is_it_a_bst(root.left,floor,root.val) and is_it_a_bst(root.right, root.val, ceiling)
    else:
        return False


print(is_it_a_bst(tree, float("-inf"), float("inf")))

    




















# def helper(root, left ,right):
#     print(root.val)
#     if not root:
#         return True

#     if left <= root.val <= right:

#         return helper(root.left, left, root.val) and helper(root.right, root.val, right)
#     else: 
#         return False

# print(helper(tree,float("-inf"), float("inf")))

























# def helper(root,left, right):

#     if not root.left and not root.right:
#         return True
    
#     if root.val <= root.left.val or root.val >= root.right.val:
#         return False
    
#     return helper(root.left, left, root.val) and helper(root.right, root.val, right)

# print(helper(tree, float('-inf'), float('inf')))