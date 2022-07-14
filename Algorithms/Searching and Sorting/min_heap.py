
class MinHeap:
    def __init__(self, capacity) -> None:
        self.capacity= capacity
        self.heap = []
        self.size = 0

    
    def parent(self,i):
        return (i-1)//2

    def left_child_index(self,i):
        return (i*2)+1

    def right_child_index(self,i):
        return (i*2 +1)

    def has_parent(self,index):
        return self.parent(index) >=0
    
    def hasLeftChild(self, index):
        return self.left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.right_child_index(index)<self.size

    def is_full(self):
        return self.size == self.capacity

    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]


    def insert(self, item):
        if self.is_full():
            print("is full")
            return 
    
        self.heap.append(item)
        self.size += 1
        self.heapifyup()

    def heapifyup(self):
        print("heapify called")
        index = self.size-1

        while self.has_parent(index) and self.heap[self.parent(index)] > self.heap[index]:
            print(" inside while")
            parent_index = self.parent(index)

            self.swap(self.heap, index, parent_index)
            index = parent_index

    def view(self):
        return self.heap

min_heap = MinHeap(20)
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(1)


print(min_heap.view())



    

    

    




