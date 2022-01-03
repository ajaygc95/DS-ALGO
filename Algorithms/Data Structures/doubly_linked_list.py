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

        if not self.head:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
        else:
            new_node = Node(data)
            prev = None
            temp = self.head

            while temp:
                prev = temp
                temp = temp.next
            
            prev.next = new_nodeggit 
            new_node.next = None

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
dll.append(6)
dll.prepend(0)

dll.view()