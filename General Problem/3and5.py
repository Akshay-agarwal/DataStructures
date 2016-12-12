def palindrome(n):
    temp=n
    a=0
    while temp!=0:
        a=temp%10+a*10
        temp=int(temp/10)

    if(n==a):
        return "Palindrome"

    else:
        return "Not Palin"

a=palindrome(12321)
print(a)
