def rev_word(s):
    s = s.split()
    temp = ''
    for words in reversed(range(len(s))):
        temp = temp + (s[words]) + ' '
    return temp.rstrip()

print(rev_word("Akshay is a good boy   aa"))

#One line solutions

def rev_words(s):
    return " ".join(reversed(s.split()))

print(rev_words("Akshay is a good boy   aa"))

def rev_wor(s):
    return " ".join(s.split()[::-1])

print(rev_word("Akshay is a good boy   aa"))

# This is solution with the right algorithms
def rev_sen(s):
    word = []
    length = len(s)
    space = [' ']
    i = 0

    while i < length:
        if s[i] not in space:

            word_start = i

            while i < length and s[i] not in space:
                i = i +1
            word.append(s[word_start:i])
        i +=1

    return ' '.join(reversed(word))


sent = 'My wanna se you i lie        '
print(rev_sen(sent))

#This is solution where we print exact reverse
def rev_sen(s):
    word = []
    length = len(s)
    space = [' ']
    i = 0

    while i < length:
        if s[i] not in space:

            word_start = i

            while i < length and s[i] not in space:
                i = i +1
            word.append(s[word_start:i][::-1])#this is the change
        i +=1

    return ' '.join(reversed(word))


sent = 'My wanna se you i lie        '
print(rev_sen(sent))


