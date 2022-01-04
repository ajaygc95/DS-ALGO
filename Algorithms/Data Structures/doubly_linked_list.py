class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None

    # def append(self,data):
 
    #     if not self.head:
    #         new_node = Node(data)
    #         new_node.prev = None
    #         self.head = new_node
    #     else:

    #         new_node = Node(data)
    #         temp = self.head
    #         while temp.next:
    #             temp = temp.next
            
    #         temp.next = new_node
    #         new_node.prev = temp
    #         new_node.next = None



    # def prepend(self,data):
    #     if not self.head:
    #         new_node = Node(data)
    #         new_node.prev = None
    #         self.head = new_node
    #     else:
    #         new_node = Node(data)
    #         temp = self.head

    #         new_node.next = temp
    #         new_node.prev = None
    #         self.head = new_node
    #         temp = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = None
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = None
            self.head = new_node
            new_node.prev = None
        else:
            temp = self.head

            new_node.next = temp
            new_node.prev = None
            self.head = new_node
            
    def add_after(self, place, data):
        #if it's the last nod eyou can jsut append()
        new_node = Node(data)

        temp = self.head 
        prev = None
         
        while temp and temp.val != place:
            prev = temp
            temp = temp.next
        if not temp: 
            return False
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = prev

    
    def add_before(self, place, data):
        #if it's the first node you can prepend() 
        new_node = Node(data)
        temp = self.head
        prev = None
        while temp and temp.val != place:
            prev = temp
            temp = temp.next

        prev.next = new_node
        new_node.next = temp
        new_node.prev =prev

    def delete(self,data):
        temp = self.head
        
        if not self.head:
            return 
        
        if self.head.val == data:
            self.head = None

        prev = None

        while temp and temp.val != data:
            prev  = temp
            temp = temp.next
        
        prev.next = temp.next
        if temp.next:
            temp.next.prev = prev
        
        temp = None



    def view(self):
        temp = self.head
        while temp :
            print(temp.val, end=" --> ")
            temp = temp.next
        print("None")


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

dll.append(7)
dll.append(9)
dll.prepend(0)

dll.add_before(7,6)
dll.add_after(7,8)

dll.delete(8)


dll.view()