def triangleNum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        i+=1
    return sum
def divisor(m):
    l=[]
    j=1
    for j in range(1,m+1):
        if m%j==0:
            l.append(j)
    return l



def noOfDivisors(n):
    i=1
    while len(divisor(triangleNum(i)))<n:
        i=i+1
    return triangleNum(i)


print(noOfDivisors((500)))


'''

for i in range(1,100):

 print(triangleNum(i),":",len(divisor(triangleNum(i))))


'''
