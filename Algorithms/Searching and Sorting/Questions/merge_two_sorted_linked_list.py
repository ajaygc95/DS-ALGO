class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        new_node = ListNode(item)
        if not self.head:
            self.head = new_node
            return 
        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = new_node

    def view(self):
        curr = self.head
        while curr:
            print(curr.val, end='--> ')
            curr = curr.next
        print("None")


list1 = LinkedList()

list1.insert(1)
list1.insert(4)
list1.insert(5)

list2 = LinkedList()

list2.insert(1)
list2.insert(3)
list2.insert(4)

list1.view()
list2.view()


def merge_two_list(list1, list2):
    
    sentinel = ListNode()
    dummy = sentinel
    while list1 and list2:
        print(sentinel.val, list1.val, list2.val)
        if list1.val <= list2.val:
            sentinel.next = list1
            list1 = list1.next
        else:
            sentinel.next = list2
            list2 = list2.next
        sentinel = sentinel.next
    
    if list1:
        sentinel.next = list1
    
    if list2:
        sentinel.next = list2
    
    return dummy.next

result = merge_two_list(list1.head, list2.head)

while result:
    print(result.val, end='-->')
    result = result.next
print("None")

