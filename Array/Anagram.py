def anagram(s1,s2):
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    d = {}
    for letter in s1:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    for letter in s2:
        if letter in d:
            d[letter] -= 1
        else:
            d[letter] = 1

    for i in d:
        if d[i] != 0:
            return i
    return True

print(anagram('go3 d','Do3g'))
print(anagram('clint eastwo(od','old( west action'))
print(anagram('12324','12345'))

