class Node(object):
    def __init__(self,value,next):
        self.value=value
        self.next=next

class LinkedList(object):
    def __init__(self):
        self.start = None
        self.end = None
        self.length=0

    def append(self,value):
        n= Node(value, None)

        if self.start is None:
            self.start = n
            self.length=self.length+1
        else:
            self.end.next = n
            self.length=self.length+1
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
        s='['
        current = self.start
        while current is not None:
            s= s+ str(current.value)+','
            current=current.next
        s= s+']'
        return s

    def delete(self,i):
        n=self.getN(i)
        current = self.start

        if i == 1:
            self.start=current.next

        else:
            for j in range(i):
                if j is i-1:
                    current.next=n.next
                else:
                    current=current.next

        self.length = self.length-1

    def k_last(self,i):
        self.start= self.getN(i)








