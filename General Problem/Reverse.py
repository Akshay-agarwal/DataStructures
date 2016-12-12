def Reverse(sentence):
    sentence=sentence.split()
    new_sentence=""
    for i in reversed(range(len(sentence))):
        new_sentence=new_sentence+" "+sentence[i]

    return  new_sentence

user_sentence=input("Enter a sentence that you want to reverse : ")
result=Reverse(user_sentence)
print(result)
