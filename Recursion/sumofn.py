def recSum(n):
    if n==1:
        return 1
    else:
        return n+recSum(n-1)

print((recSum(10)))
