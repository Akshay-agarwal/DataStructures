def selectionSort(arr):
    temp = 0;

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

s = selectionSort([1,24,5,22,6,3])
print(s)
print(selectionSort([5,3,1,2,4]))
