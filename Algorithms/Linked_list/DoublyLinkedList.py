class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addAtHead(self, val):

        new_node = Node(val)

        if not self.head:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
            return 
        else:
            temp = self.head
            new_node.prev = None
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node

    def addAtTail(self,val):
        new_node = Node(val)

        if not self.head:
            new_node.prev = None
            new_node.next = None

            self.head = new_node
            return 
        temp = self.head
        prev = None
        while temp:
            prev = temp
            temp = temp.next

        prev.next = new_node
        new_node.prev = prev
        new_node.next = None

    def addAtIndex(self, index, val):
        new_node = Node(val)
        if not self.head and index != 0:
            return 

        if not self.head and index == 0:
            new_node.prev = None
            new_node.next = None

            self.head = new_node
            return 
        
        temp = self.head
        count = 1
        prev = None

        while temp:

            if count == index:
                new_node.prev = prev
                prev.next = new_node
                new_node.next = temp
                temp.prev = new_node

            prev = temp 
            temp = temp.next
            count += 1
    
    def deleteAtIndex(self,index):

        if not self.head:
            return 
        temp = self.head

        if index == 0:
            self.head = temp.next
            self.head.prev = None

        prev = None
        count = 0

        while temp:
            if count == index:
                prev.next = temp.next
                temp.next.prev = prev
                temp.prev = None
                temp.next = None
                return 
            count += 1
            prev = temp
            temp = temp.next
            


    def view(self):
        temp = self.head

        while temp:
            print(temp.val,end=" --> ")
            temp= temp.next

        print("None")


ll = LinkedList()
ll.addAtHead(1)
ll.addAtHead(2)
ll.addAtTail(3)
ll.addAtTail(4)
ll.addAtIndex(3, 6)
ll.view()
ll.deleteAtIndex(2)

ll.view()