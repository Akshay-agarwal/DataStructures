'''
n → n/2 (n is even)
n → 3n + 1 (n is odd)

'''


def coll(n):

    l=[]
    l.append(n)
    while n != 1:
        if (n%2)==0:
            n=(n/2)
            l.append(n)

        else:
            n=((3*n)+1)
            l.append(n)

    return len(l)


for i in range(2,2000000):
    m=[]
    m.append(coll(i))
    if(m.append(coll(i))==185):
        print(i)

print(max(m))
