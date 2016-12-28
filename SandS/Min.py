def max(arr):
    current_max = arr[0]
    for i in range(len(arr)):
        if arr[i]>=current_max:
            current_max = arr[i]
            positon = i

    return current_max,positon

def min(arr):
    current_min = arr[0]
    for i in range(len(arr)):
        if arr[i]<=current_min:
            current_min = arr[i]
            positon = i
    return current_min,positon

ma = max([2,2,3,4,5,6,7,8,9,10,11,12,-3,-4,197])
print(ma)
min = min([-1766,2,3,4,5,6,7,8,9,10,11,12,-3,-4,-7])
print(min)




