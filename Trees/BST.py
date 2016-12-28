class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.val == data:
            return False

        elif self.val > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.val == data:
            return True

        elif self.val > data:
            if self.left:
                return self.left.find(data)
            else:
                return False

        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.val))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
            print(str(self.val))

    def inorder(self):
        if self:
            if self.left:
                self.left.preorder()
            print(str(self.val))
            if self.right:
                self.right.preorder()


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preoder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("Inorder")
        self.root.inorder()



t = Tree()
t.insert(20)
t.insert(12)
t.insert(24)
t.insert(9)
t.insert(15)
t.insert(14)
t.insert(18)
t.insert(27)
t.insert(16)
t.insert(28)
t.insert(22)
t.insert(26)
t.preoder()
t.inorder()
t.postorder()
