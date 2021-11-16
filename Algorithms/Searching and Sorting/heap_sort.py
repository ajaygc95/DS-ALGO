

def swap(a,b,arr):
    arr[a], arr[b] = arr[b], arr[a]



"""
parent = floor( Index -1 / 2) 
left_chiled = 2*index + 1
right_child = 2*index + 2

"""

class Heap:

    def __init__(self) -> None:
        self.heaplist = [0]
        self.size = 0
    

    def parentIndex(self,index):
        return (index-1//2)
    
    def leftChildIndex(self,index):
        return ((2*index)+1)

    def rightChildIndex(self, index):
        return ((2*index)+2)


    def hasParent(self,index):
        return self.parentIndex(index)>=0

    def hasLeftChild(self,index):
        return self.leftChildIndex(index) < self.size


    def hasRightChild(self,index):
        return self.rightChildIndex(index) < self.size

    def parent(self,index):
        return self.heaplist[self.parentIndex(index)]
    
    def leftChild(self,index):
        return self.heaplist[self.leftChildIndex(index)]
    
    def rightChilde(self, index):
        return self.heaplist[self.rightChildIndex(index)]

    def insert(self,index):
        self.heaplist.append(index)
        self.size += 1
        self.heapifyup(self.size)

    def heapifyup(self, size):

        while size//2 > 0:

            if self.heaplist[size] < self.heaplist[size//2]:
                swap(size, size//2, self.heaplist)

            size = size//2


heap = Heap()

heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(5)


print(heap.heaplist)



# def swap(a,b,arr):
#     arr[a], arr[b] = arr[b], arr[a]

# class Heap:
#     def __init__(self) -> None:
#         self.heaplist = [0]
#         self.size = 0

#     def percup(self, size):
#         print(f"size: {size} size//2: {size//2}")
        
#         while size//2>0:
#             if self.heaplist[size] < self.heaplist[size//2]:
#                 swap(size, size//2, self.heaplist)
#             size = size//2

#     def percDown(self,size):
#         while (size*2) <= self.size:
#             min_child = self.minChild(size)

#             if self.heaplist[size] > self.heaplist[min_child]:
#                 swap(size,min_child,self.heaplist)
#             size = min_child
            
#     def minChild(self,i):
#         if i*2+1 > self.size:
#             return i*2
#         else:
#             if self.heaplist[i*2] < self.heaplist[i*2+1]:
#                 return i*2
#             else:
#                 return i*2+1

#     def insert(self,item):
#         print("inserting ", item)
#         self.heaplist.append(item)
#         self.size += 1
#         self.percup(self.size)


#     def delMin(self):
#         minItem = self.heaplist[1]
#         self.heaplist[1] = self.heaplist[self.size]
#         self.size -= 1
#         self.heaplist.pop()
#         self.percDown(1)
#         return minItem

#     def buildHeap(self, alist):
#         i = len(alist)//2
#         self.size = len(alist)
#         self.heaplist = [0] + alist[:]
#         while i > 0:
#             self.percDown(i)
#             i -= 1

        
# heap = Heap()
# i = [0, 9, 5, 6, 2, 3]

# heap.buildHeap(i)
# print(heap.heaplist)




