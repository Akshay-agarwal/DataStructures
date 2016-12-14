def sum(num):
    if num ==0:
        return 0

    elif num == -1:
        return -1

    else:
        return num+sum(num-2)

print(sum(10))
