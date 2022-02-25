class Node:

    def __init__(self, data) -> None:
        self.val = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert(self, key):
        new_node = Node(key)

        if self.head == None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def remove(self):
        pass

    def view(self):

        temp = self.head

        while temp:
            print(temp.val)
            temp = temp.next
        

ll1 = LinkedList()
ll1.insert(1)
ll1.insert(2)
ll1.insert(3)
ll1.insert(4)
ll1.view()
        