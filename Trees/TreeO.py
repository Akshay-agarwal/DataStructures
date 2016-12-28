class TreeO(object):

    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = newNode

        else:
            t = TreeO(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = newNode

        else:
            t = TreeO(newNode)
            t.right = self.right
            self.right = t

    def setRoot(self,newRoot):
        self.root = newRoot

    def getRoot(self):
        return self.root

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

t = TreeO(5)
print(t.getRoot())
print(t.getLeft())
t.insertLeft(2)
t.insertRight(6)
print(t.getLeft())
print(t.getLeft())
t.insertLeft(4)
t.insertLeft(43)
t.insertLeft(12)
t.insertLeft(45)
print(t.getLeft())
t.insertRight(26)
t.insertRight(66)
t.insertRight(46)
t.insertRight(61)
print(t.getLeft())


