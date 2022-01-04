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

    def swap(self, first, second):

        if first == second:
            return
         
        temp1 = self.head
        prev1 = None

        while temp1 and temp1.val != first:
            prev1 = temp1
            temp1 = temp1.next
        
        # print(f"{temp1.val} and {prev1.val}")

        temp2 = self.head
        prev2 = None

        while temp2 and temp2.val != second:
            prev2 = temp2
            temp2 = temp2.next
        
        if prev1:
            prev1.next = temp2
        else:
            self.head = temp2
        if prev2:
            prev2.next = temp1
        else:
            self.head = temp1
        
        temp1.next , temp2.next = temp2.next , temp1.next

        # print(f'{prev2.val} --> {temp2.val}')


    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def view(self):
        temp = self.head
        while temp:
            print(temp.val,end=" --> ")
            temp = temp.next
        print("None")

    # def reverse(self):
    #     prev = None
    #     temp = self.head

    #     while temp :
    #         holder = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = holder

    #     self.head = prev




    def reverse(self):

        temp = self.head
        prev = None
        while temp:
            holder = temp.next
            temp.next = prev
            prev = temp
            temp = holder
        
        self.head = prev



ll = LinkedList()
ll.insert(5)
ll.insert(6)
ll.insert(8)

ll.prepend(4)

ll.insert_after_node(7,6)

# ll.view()
# # ll.delete()
# ll.delete_at_position(0)
ll.view()
# ll.swap(4,6)

# print(ll.length())
ll.reverse()
ll.view()