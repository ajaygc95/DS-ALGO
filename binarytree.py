class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, item):
        if self.data == item:
            return
        if self.data == None:
            self.data = item
        if item < self.data: 
            if self.left:
                self.left.insert(item)
            else:
                self.left = BinaryTree(item)
        if item > self.data:
            if self.right:
                self.right.insert(item)
            else:
                self.right = BinaryTree(item)
       

    def printdata(self):
        elements = []


        while self.right:
            elements += self.right.printdata()
            self.right = self.right.right

        elements.append(self.data)
        
        while self.left:
            elements += self.left.printdata()
            self.left = self.left.left

        return elements



if __name__ == "__main__":
    bt = BinaryTree(20)
    numbers = [1,6,30,20,0,8,50,35,37,27,3,2]
    for n in numbers:
        bt.insert(n)
    print(bt.printdata())