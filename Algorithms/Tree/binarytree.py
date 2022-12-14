class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, key):

        new_node = Tree
       

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