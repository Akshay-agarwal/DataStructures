import random

def AddSand(func):
    def Add_sand():
        return func()+ 2
    return Add_sand

def hamAdd():
    return 5

hamAdd = AddSand(hamAdd)
print(hamAdd())

hamAdd = AddSand(hamAdd)
print(hamAdd())

