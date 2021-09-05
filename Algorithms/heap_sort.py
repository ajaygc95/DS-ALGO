class Heap:
    def __init__(self, array):
        self.array  = [-1] + array
        self.size = len(array)
        self.buildheap()

    def parent(self, i):
        return i/2
    
    def leftchild(self,i):
        if 2*i < len(self.array):
            return 2*i
        else:
            return -1

    def rightchild(self,i):
        if 2*i +1 <len(self.array):
            return 2*i + 1
        else:
            return -1

    def getsmallerchild(self,i):
        res = -1
        if self.leftchild(i) != -1:
            res = self.leftchild(i)
        
        if self.rightchild(i) != -1:
            if res == -1:
                res = self.rightchild(i)
            else:
                if self.array[res] > self.array[self.rightchild(i)]:
                    res = self.rightchild(i)
        return res