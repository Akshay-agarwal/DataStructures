def harmRec(n):
    if n == 1:
        return 1
    else:
        return (1/n)+harmRec(n-1)

print(harmRec(5))
