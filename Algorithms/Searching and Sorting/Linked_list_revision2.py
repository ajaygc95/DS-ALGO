from hashlib import new
from logging.config import valid_ident


class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    
    def insert(self, key):
        new_node = Node(key)
        if not self.head:
            self.head = new_node
            return 

        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    def insert_at_index(self, index, item):

        new_node = Node(item)
        temp = self.head

        if index == 0:
            self.head = new_node
            self.head.next = temp
            return 

        temp = self.head
        count = 0
        prev = None
        while temp:
            if count == index:
                prev.next = new_node
                new_node.next = temp
                return 
            count += 1
            prev = temp
            temp = temp.next



    def view(self):
        temp = self.head

        while temp:
            print(temp.val, end=" --> ")
            temp = temp.next
        
        print("None")

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert_at_index(0,4)
ll.insert_at_index(2,5)
ll.view()