def urlify(s,l):

    new_length = len(s)
    r = ''
    for i in reversed(range(l)):
        if s[i] == ' ':
            s[new_length-3 : new_length] = '%20'
            new_length -= 3

        else:
            s[new_length-1] = s[i]
            new_length -= 1

    return  s

print(urlify('Mr John Smith    ',13))





