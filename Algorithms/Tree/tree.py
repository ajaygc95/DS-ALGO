from abc import get_cache_token


class Tree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = []

    def add_data(self, child):
        child.parent = self
        self.child.append(child)
    
    def printdata(self):
        if self.get_level() > 0:
            padding = self.get_level() * "  "
        else:
            padding = ''
        print(f"{padding}|-- {self.data}")

        for ch in self.child:    
            ch.printdata()

    def get_level(self):
        count = 0
        p = self.parent
        while p :
            count += 1
            p = p.parent
        
        return count
            


def tree():
    root = Tree('Soccer Clubs')

    country1 = Tree("English")
    country1.add_data(Tree("English"))
    country1.add_data(Tree("English"))
    country1.add_data(Tree("English"))
    country1.add_data(Tree("English"))


    country2 = Tree("Spain")
    country2.add_data(Tree("Spain"))
    country2.add_data(Tree("Spain"))
    country2.add_data(Tree("Spain"))

    root.add_data(country1)
    root.add_data(country2)

    return root

if __name__ == '__main__':
    tree().printdata()