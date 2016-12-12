def sumofPower(number,n):
    temp=number**n

    sum=0
    while temp>0:
        sum=sum+temp%10
        temp=int(temp/10)
    return sum

print(sumofPower(2,10))
