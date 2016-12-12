class Node(object):

    def __init__(self,prev,value, next):
        self.value = value
        self.next = next
        self.prev = prev

class Doublell(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head(self,element):

        n = Node(None,element,None)
        self.length += 1

        if self.head is None:
            self.head = n
            self.tail = n

        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def insert_tail(self,element):

        n = Node(None,element,None)
        self.length += 1

        if self.tail is None:
            self.head = n
            self.tail = n

        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def getN(self,i):

        current = self.head
        j=1
        for j in range(1,i):
            if current is None:
                return None
            else:
                current = current.next
        return current

    def delete_head(self):

        if self.head is None:
            return "Cannot delete from Empty Linked List"

        else:
            self.head = self.head.next

        self.length -= 1

    def delete(self,i):


        if self.head is None:
            return "Cannot delete from Empty Linked List"

        current = self.head

        if i == 1:
            self.head = self.head.next

        elif i == (self.length):

            self.tail.prev.next = None

        elif i > self.length:
            return "Please enter a value in the range of list"

        else:
            n = self.getN(i)
            n.prev.next = n.next
            n.next.prev = n.prev

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




s = Doublell()
s.insert_head(2)
s.insert_head(3)
s.insert_head(4)
s.insert_head(5)
s.insert_tail(6)
s.insert_tail(7)
s.insert_tail(6)
s.insert_tail(5)
s.insert_head(2)
s.delete(5)
print(s)
print(s.listlength())
#[2-->5-->4-->3-->2-->6-->7-->6-->5-->]
