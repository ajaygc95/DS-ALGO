class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.size = 0
        self.min = [] #Minimum Element to my left, including myself.
    

    def push(self,key):
        if self.size == 0:
            self.min.append(key)
        else:
            self.min.append(self.smaller(key,self.min[self.size-1]))
        
        self.stack.append(key)
        self.size += 1

    def smaller(self,a,b):
        if a < b:
            return a
        else:
            return b
    
    def pop(self):
        del self.min(self.size-1)
        del self.stack(self.size-1)
        self.size -= 1

    def top (self):
        return self.stack[self.size-1]

    def getMin(self):
        return self.min(self.size-1)

    


