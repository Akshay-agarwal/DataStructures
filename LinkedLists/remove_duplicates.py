from linkedlist import LinkedList

def dupRemove(n):
    d={n.value:1}
    current = n
    while current.next is not None:
        if current.next.value in d:
            current.next = current.next.next
        else:
            d[current.value]=1
            current = current.next


l= LinkedList()

l.append(1)
l.append(2)
l.append(3)
l.append(5)
l.append(3)
l.append(2)
l.append(10)
l.append(153)
l.append(15)
dupRemove(l.start)
print(l)
# print(l.getN(1).value)
# print(l.getN(0).value)
# l.k_last(3)
# #l.delete(3)
# print(l)
# print(l.len())

