class Node(object):
    def __init__(self,previous,value,next):
        self.value=value
        self.previous=previous
        self.next=next

class LinkedList(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.length=0

    def append(self,value):
        n= Node(None, value, None)
        self.length=self.length+1

        if self.start is None:
            self.start = n

        else:


            self.end.next = n
            n.previous=self.end


        self.end = n


    def getN(self,i):
        current = self.start

        for j in range(i):
            if current is None:
                return None
            else:
                current= current.next
        return current

    def len(self):
        return self.length

    def __str__(self):
        s = '['
        current = self.start
        while(current is not None):

            str(current.value)
            s = s + str(current.value)+ ','
            current = current.next

        s=s+']'
        return s

    def delete(self,i):
        current = self.start
        n=self.getN(i)
        if i == 0:
            self.start = n.next

        elif i == self.length-1:
            n.previous.next = None
            self.end = n.previous

        else:
            n.previous.next=n.next
            n.next.previous=n.previous

        self.length -=1

l= LinkedList()
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.delete(0)
print(l)
l.delete(1)
print(l)
print(l.len())
