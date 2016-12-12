def isPrime(n):
    for i in range(2,int(n+1/2)):
        if n%i==0:
            return False
            break

    return True


def nthPrime(n):
    prime=1
    sum=0
    while prime<n:
        prime+=1
        if isPrime(prime):
            sum=sum+prime
    return sum

print(nthPrime(2000000))


