name=input("Enter your name :")
age=int(input("Enter your age :"))
years_2_hundred=(100-age)
print(name+" You will be 100 in ",years_2_hundred," years ")
num=int(input("Enter no of times you want the message to be printed"))
for i in range(0,num):
    print(i+1," ."+name+" You will be 100 in ",years_2_hundred," years ")
