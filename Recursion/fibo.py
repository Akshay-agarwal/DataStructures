def recFibo(n):
    if n == 0:
        return 0

    elif n ==1:
        return 1

    else:
        
        return recFibo(n-1)+recFibo(n-2)

print(recFibo(5))
