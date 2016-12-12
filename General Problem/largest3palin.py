list=[]

def palin(n):
    temp=n
    a=0
    while temp!=0:
        a=temp%10+a*10
        temp=int(temp/10)
    if a==n:
        return "Palin"
    else:
        pass

for i in reversed(range(100)):
    for j in reversed(range(1000)):
        n=i*j
        if palin(n):
            list.append(n)
print(list)

'''
for k in list:
    palinlist=[]
    a=0
    temp=list[k]
    while temp!=0:
        a=temp%10+a*10
        temp=int(temp/10)

    if(list[k]==a):
        palinlist.append(a)

    else:
        pass


print(palinlist)
'''
