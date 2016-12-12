from linkedlist import LinkedList

def delmiddle(n,i):
    current = n.start
    prev = None
    while current:

       if current.value == i:
           prev.next = current.next
           n.length -= 1
           return True
       else:
           prev = current
           current = current.next


    return False






l= LinkedList()

l.append(1)
l.append(2)
l.append(3)
l.append(5)
l.append(3)
l.append(2)
l.append(10)
print(l.len())
delmiddle(l,10)
print(l.len())


# delmiddle(l,1)
print(l)
