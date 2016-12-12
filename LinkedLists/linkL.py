class Node(object):
    def __init__(self, d, n):
        self.data = d
        self.next = n

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.start = None
        self.length = 0

    def append(self, d):
        new_node = Node(d, self.start)
        self.start = new_node
        self.length += 1

    def remove(self, d):
        current = self.start
        prev_node = None

        while current:
            if current.getData() == d:
                if prev_node:
                    prev_node.setNext(current.getNext())
                else:
                    self.start = current.getNext()
                self.length -= 1
                return True
            else:
                prev_node = current
                current = current.getNext()
        return False

    def __str__(self):
        current = self.start
        s = '['
        while current:
            s = s + str(current.getData()) + '->'
            # current = current.setNext(current.getNext())
            current = current.getNext()
        s = s + ']'
        return s


l = LinkedList()

l.append(4)
l.append(3)
l.append(2)

print(l)
print(l.remove(2))
print(l)
