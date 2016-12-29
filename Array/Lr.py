arr = [1,2,3,4,5,6,7]
order = 2

for i in range(order):
    j = len(arr)-1
    while j > 0:
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j -= 1
print(arr)
