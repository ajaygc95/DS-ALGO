class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def view(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")


ll1 = LinkedList()

ll1.insert(1)
ll1.insert(3)
ll1.insert(5)

ll2 = LinkedList()
ll2.insert(3)
ll2.insert(4)

ll3 = LinkedList()
ll3.insert(7)


def merge(arr1, arr2):
    dummy = Node(0)
    final = dummy #Final is just temp , this means that you can are just pointing l1 to different node by sorting

    if not arr1:
        return arr2
    if not arr2:
        return arr1
    while arr1 and arr2:
        if arr1.data <= arr2.data:
            # print(final.data, "-->", arr1.data)
            final.next = arr1
            arr1 = arr1.next
        else:
            # print(final.data, "-->", arr2.data)
            final.next = arr2
            arr2 = arr2.next
        final = final.next  # This one is moving Node(0) to arr1(whole thing)


    if arr1:
        # print(final.data, "-->", arr1.data)
        final.next = arr1

    else:
        # print(final.data, "-->", arr2.data)
        final.next = arr2

    while final :
        final = final.next
    return final


merge(ll1.head, ll2.head)
print(ll1.head.data)
ll1.view()
