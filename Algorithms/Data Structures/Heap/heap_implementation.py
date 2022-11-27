
data = [1,2,3,4,5,6]

def swap(arr, a, b):
    arr[a], arr[b]  = arr[b], arr[a]

class Heap:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def insert(self, key):
        self.data.append(key)
        self.heapify_up(self.size)
        self.size += 1

    def get_parent_index(self,index):
        return (index-1)//2
        
    def has_parent(self, index):
        if self.get_parent_index(index) >= 0:
            return True
        return False

    def remove(self):
        print("===== removing=====", self.data[0])
        data = self.data[0]
        swap(self.data, 0, self.size-1)
        self.data.pop()
        self.size -= 1
        self.heapify_down(0)
        return data

    def left_child(self, index):
        return (index*2+1) < self.size
    
    def right_child(self, index):
        return (index*2+2) < self.size

    def heapify_up(self, index):
        parent_index = (index-1)//2
        if parent_index >= 0:
            if self.data[index] < self.data[parent_index]:
                swap(self.data, parent_index, index)
                self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest=index
        left_index = (index*2+1)
        right_index = (index*2+2)

        if self.left_child(index) and self.data[smallest] > self.data[left_index]:
            smallest = left_index
        
        if self.right_child(index) and self.data[smallest] > self.data[right_index]:
            smallest = right_index

        if index != smallest:
            swap(self.data, index, smallest)
            self.heapify_down(smallest)


    def view(self):
        print(self.data)


heap = Heap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(8)
heap.insert(0)

heap.remove()
heap.remove()
heap.view()



        






    