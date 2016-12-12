def finder(arr1,arr2):

    d = {}
    for i in range(len(arr1)):
        if arr1[i] in d:
            d[arr1[i]] += 1
        else:
            d[arr1[i]] = 1

    for j in range(len(arr2)):
        if d[arr2[j]] in d:
            d[arr2[j]] -= 1
        else:
            d[arr2[j]] = 1

    for i in d:
        if d[i] != 0:
            return i

#pythonic Solution


def find(arr1, arr2):

    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]
