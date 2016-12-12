def sumOfSquare(n):
    sum=0
    for i in range(n+1):
        sum=sum + i*i
        i=i+1
    return sum

def squareofSum(n):
    ss=0
    for j in range(n+1):
        ss=ss+j
        j=j+1
    return (ss*ss)

print(squareofSum(100)-sumOfSquare(100))

