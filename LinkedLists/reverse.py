from singlell import Singlell

def reverse(n):

    next = None
    prev = None
    current = n.head

    while current:

        next = current.next
        current.next = prev
        prev = current
        current = next
    n.head = prev


s = Singlell()
s.insert_head(2)
s.insert_head(3)
s.insert_head(4)
s.insert_head(5)
s.insert_tail(6)
s.insert_tail(7)
s.insert_tail(6)
print(s)
reverse(s)
print(s)
