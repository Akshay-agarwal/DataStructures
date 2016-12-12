from singlell import Singlell

def ktoLast(n,k):

    p1 = n.head
    p2 = n.head

    for i in range(k):
        p1 = p1.next


    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next

    return p2.value



s = Singlell()
s.insert_head(2)
s.insert_head(3)
s.insert_head(4)
s.insert_head(5)
s.insert_tail(12)
s.insert_tail(7)
s.insert_tail(6)
print(s)
print(ktoLast(s,1))
#[5-->4-->3-->2-->6-->7-->6-->]
