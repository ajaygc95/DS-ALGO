class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, key):
        if not self.head:
            self.head = Node(key)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(key)
    
    def view(self):
        temp = self.head

        while temp:
            print(temp.val,end="--> ")
            temp = temp.next
        print("None")


tree = LinkedList()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.view()