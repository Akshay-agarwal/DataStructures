def prime(num):
    count=0
    for i in range(2,num-1):
        if num%2==0:
            count+=1
    if count==0:
        prime("The number is Prime")
    else:
        print("Non Prime")

num=int(input("Enter a number, that you want to check is prime or not : "))
prime(36)
