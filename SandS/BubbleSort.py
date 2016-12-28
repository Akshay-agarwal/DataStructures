def BubbleSort(arr):
    n = len(arr)
    while n > 1:
        i = 1
        while i < n:
            if arr[i] < arr[i-1]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
            i += 1
        n -=1
    return arr

print(BubbleSort([5,1,4,3,6,9,0,2]))

