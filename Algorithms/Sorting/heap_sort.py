def swap(a,b,arr):
    arr[a], arr[b] = arr[b], arr[a]

class Heap:
    def __init__(self) -> None:
        self.heaplist = [0]
        self.size = 0

    def percup(self, size):
        print(f"size: {size} size//2: {size//2}")
        
        while size//2>0:
            if self.heaplist[size] < self.heaplist[size//2]:
                swap(size, size//2, self.heaplist)
            size = size//2

    def percDown(self,size):
        while (size*2) <= self.size:
            min_child = self.minChild(size)

            if self.heaplist[size] > self.heaplist[min_child]:
                swap(size,min_child,self.heaplist)
            size = min_child
            
    def minChild(self,i):
        if i*2+1 > self.size:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1

    def insert(self,item):
        print("inserting ", item)
        self.heaplist.append(item)
        self.size += 1
        self.percup(self.size)


    def delMin(self):
        minItem = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return minItem

    def buildHeap(self, alist):
        i = len(alist)//2
        self.size = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

        
heap = Heap()
i = [0, 9, 5, 6, 2, 3]

heap.buildHeap(i)
print(heap.heaplist)




