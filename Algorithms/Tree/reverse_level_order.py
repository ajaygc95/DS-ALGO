print(4%2)
# class Node:
#     def __init__(self, val ) -> None:
#         self.val = val
#         self.right = None
#         self.left = None

#     def insert(self, item):
#         new_node = Node(item)
#         if self.val is None:
#             self.val = new_node
#             return
        
#         if item < self.val:
#             if self.left:
#                 self.left.insert(item)
#             else:
#                 self.left = new_node

#         else:
#             if self.right:
#                 self.right.insert(item)
#             else:
#                 self.right = new_node

#     def in_order(self):
#         elements = []
#         print(self.val)
#         if self.left:
#             elements += self.left.in_order()

#         elements.append(self.val)
#         if self.right:
#             elements += self.right.in_order()
#         return(elements)

# tree = Node(0)
# tree.left = Node(1)
# tree.left.left  = Node(3)
# tree.left.right = Node(4)
# tree.right = Node(2)


# visited = [-1] * 6


# def helper(root):
    


# print(visited)