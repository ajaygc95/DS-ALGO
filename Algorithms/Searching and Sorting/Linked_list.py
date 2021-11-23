from collections import deque

class Node:

    def __init__(self,val) -> None:
        self.val = val
        self.next = None



class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert(self, item):

        if not self.head:
            self.head = Node(item)
            return

        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = Node(item)
        
    def view(self):

        temp = self.head

        while temp.next:
            print(temp.val,end=" --> ")
            temp = temp.next
        print(temp.val, end=" --> ")
        print(temp.next)



ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)


def helper(root):

    prev = None

    while root.next:

        curr = root.next
        root.next = prev
        prev = root
        root = curr
    root.next = prev
    return root

helper(ll)

ll.view()