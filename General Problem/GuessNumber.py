import random
number=random.randrange(1,100)
incorrect=True
count=0
while incorrect:
    guess=int(input(" Make a guess : "))
    count+=1
    if guess>number:
        print("Too high")
    elif guess<number:
        print("Too low")
    else:
        print("You got it")
        print("Attempts = ",count)
        incorrect=False
