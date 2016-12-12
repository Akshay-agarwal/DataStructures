class Node(object):
    def __init__(self,previous,value,next):
        self.previous = previous
        self.value = value
        self.next = next

class DoubleLL(object):
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


            s = s + str(current.value)+ ','
            current = current.next

        s=s+']'
        return s
    def delete(self,i):
        n = self.getN(i)

        if n.previous == None:
             self.start=n.next
             n.next.previous = None


        elif i == self.length-1:
            self.end = n.previous
            n.previous.next = None


        else:
            n.previous.next = n.next
            n.next.previous = n.previous

        self.length = self.length-1


l = DoubleLL()
l.append(5)
l.append(4)
l.append(6)
l.append(8)
l.append(9)
l.delete(0)
l.delete(3)
print(l)
print(l.start)
print(l.getN(1).previous)



