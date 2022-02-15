# input = [41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23]
# strings = "413724102439765811101615121314191817202221233530292625272832313433363938404442434846454749"

# print(len(strings))

item1 = [1,2,None,None,3,4,None,None,5,None,None]
item2 = [1,2,None,None,3,4,None,None,5,None,None,]



item = "2"

print(int(item))

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

#         if self.left:
#             elements += self.left.in_order()

#         elements.append(self.val)
#         if self.right:
#             elements += self.right.in_order()
#         return(elements)

# node1 = Node(3)
# node1.left = Node(2)
# node1.left.left = Node(1)
# node1.right = Node(4)

# node2 = Node(6)
# node2.left = Node(5)
# node2.right = Node(7)

# store1 = node1.in_order()
# store2 = node2.in_order()
# final = store1 + store2

# def helper(arr, start, end):
#     if start > end:
#         return None
#     if start == end:
#         return Node(arr[start])
#     mid = (start + end)//
#     print(final[mid])
#     new_root = Node(arr[mid]) 
#     new_root.left = helper(arr, start, mid)
#     new_root.right = helper(arr, mid+1, end)
#     return new_root
# store = helper(final, 0 , len(final)-1)
# store.in_order()

