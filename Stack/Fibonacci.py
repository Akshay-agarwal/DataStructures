n=int(input("Please Enter how many numbers in Fibonacci series you want : "))
a=0
b=1
c=0
print(a)
print(b)
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
