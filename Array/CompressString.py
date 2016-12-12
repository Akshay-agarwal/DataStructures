def compress(s):
    i = 0
    length = len(s)
    count = 0
    Compressed = ''

    if length == 0:
        return ''

    elif length == 1:
        return s+"1"


    else:
        temp = s[i]
        while i < length:
            if temp == s[i]:
                count = count+1
                i += 1

            else:
                Compressed += temp
                Compressed += str(count)
                temp = s[i]
                count = 1
                i += 1

    return Compressed+(temp+str(count))

print(compress(' AAAAbbbbbCCCC'))
