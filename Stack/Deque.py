class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pushFront(self,items):
        self.items.append(items)

    def pushRear(self,items):
        self.items.insert(0,items)

    def popFront(self):
        return self.items.pop()

    def popBack(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.pushFront(1)
d.pushFront(2)
d.pushFront(3)
d.pushFront(4)
d.pushFront(5)
print(d.size())
print(d.popFront())
print(d.popBack())
print(d.size())

