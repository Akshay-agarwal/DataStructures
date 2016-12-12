def urlify(s):
    res = ''
    start = False

    for i in reversed(s):
        if i not in ' ':
            start = True


        if start == True and i == ' ':
            res += '02%'

        else:
            res += i

    return res[::-1]

print(urlify('ab cd     ',))

