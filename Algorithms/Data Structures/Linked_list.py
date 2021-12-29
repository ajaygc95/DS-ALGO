class Node:

    def __init__(self, val) -> None:
        self.val = val
        self. next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert(self,key):

        new_node = Node(key)
        
        if not self.head:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next
        temp.next = new_node
            
    def prepend(self, key):

        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self,key, value):
        new_node = Node(key)
        
        temp = self.head

        while temp:
            if temp.val == value:
                break
            temp = temp.next
        if temp:
            new_node.next = temp.next
            temp.next = new_node 

    def delete(self, key):
        temp = self.head
        if temp and key == temp.val:
            self.head = self.head.next
            temp = None
            return

        prev = temp
        
        while temp and temp.val != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
            temp = None


    def delete_at_position(self,pos):

        temp = self.head
        prev = None
        
        if temp and pos == 0:
            self.head = temp.next
            temp = None
            return

        count = 0
       
        while temp and count != pos:
            count += 1
            prev = temp
            temp = temp.next

        if count >0:
            prev.next = temp.next
            temp = None
        
    def view(self):
        temp = self.head
        while temp:
            print(temp.val,end=" --> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.insert(5)
ll.insert(6)
ll.insert(8)

ll.prepend(4)

ll.insert_after_node(7,5)

ll.view()
# ll.delete()
ll.delete_at_position(0)
ll.view()