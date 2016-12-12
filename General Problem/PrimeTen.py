def isPrime(n):
    for i in range(2,int(n+1/2)):
        if n%i==0:
            return False
            break

    return True


def nthPrime(n):
    numberPrime=0
    prime=1

    while numberPrime<n:
        prime+=1
        if isPrime(prime):
            numberPrime+=1
    return prime

print(nthPrime(10001))


