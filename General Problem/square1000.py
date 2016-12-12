for a in range(2,1000):
    for b in range(a+1,999):
        c=(a**2+b**2)**0.5
        if a+b+c==1000:
            print("a is ",a)
            print("b is ",b)
            print("c is ",c)
            print("Product is :",a*b*c)
            break
