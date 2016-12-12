class Node(object):

    def __init__(self,value, next):
        self.value = value
        self.next = next

class Singlell(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def getN(self,i):

        current = self.head
        for j in range(1,i):
            if current is None:
                return None
            else:
                current = current.next

        return current


    def insert_head(self,element):

        n = Node(element,None)
        self.length += 1

        if self.head is None:
            self.head = n
            self.tail = n

        else:
            n.next = self.head
            self.head = n

    def insert_tail(self,element):

        n = Node(element,None)
        self.length += 1

        if self.tail is None:
            self.head = n
            self.tail = n

        else:
            self.tail.next = n
            self.tail = n

    def delete(self,i):

        if self.head is None:
            return "Cannot delete from Empty Linked List"

        if i == 1:
            self.head = self.head.next

        else:
            n = self.getN(i-1)
            n.next = n.next.next

        self.length -= 1

    def listlength(self):
        return self.length

    def __str__(self):

        s = '['
        current = self.head
        while current is not None:
            s = s + str(current.value) + '-->'
            current = current.next

        s += ']'
        return s


    # def delete(self):

# s = Singlell()
#s.insert_head(2)
# s.insert_head(3)
# s.insert_head(4)
# s.insert_head(5)
# s.insert_tail(6)
# s.insert_tail(7)
# s.insert_tail(6)
# s.delete(1)
# print(s)
# print(s.listlength())

#[5-->4-->3-->2-->6-->7-->6-->]
