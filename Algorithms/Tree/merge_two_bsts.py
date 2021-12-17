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

        if self.left:
            elements += self.left.in_order()

        elements.append(self.val)
        if self.right:
            elements += self.right.in_order()
        return(elements)


node1 = Node(3)
node1.left = Node(2)
node1.left.left = Node(1)
node1.right = Node(4)

node2 = Node(6)
node2.left = Node(5)
node2.right = Node(7)

store1 = node1.in_order()
store2 = node2.in_order()

final = store1 + store2



def helper(arr, start, end):

    if start > end:
        return None

    if start == end:
        return Node(arr[start])



    mid = (start + end)//2

    print(final[mid])

    new_root = Node(arr[mid]) 

    new_root.left = helper(arr, start, mid)

    new_root.right = helper(arr, mid+1, end)

    return new_root

store = helper(final, 0 , len(final)-1)
store.in_order()
