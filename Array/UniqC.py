def uniqc(s):
    d = { }

    if len(s) == 0:
        return "Enter a string"

    for i in range(len(s)):
        if s[i] in d:
            return False
        else:
            d[s[i]] = 1

    return True

print(uniqc('asdAS'))

