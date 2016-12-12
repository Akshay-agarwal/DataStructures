import random


l=random.sample(range(30),10)
l=[1,1,1,1,2,3,4,4,4,5,5,5]
print(set(l))

new=[val for val in set(l) if val%2==0]
print(new)
