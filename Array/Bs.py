def Bs(arr,key):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return "Element found at position : " +str(mid+1)

        elif arr[mid] < key:
            low = mid+1

        else:
            high = mid-1
    return "key not found"

b = Bs([1,2,3,4,6,8,9,11,12,34,55,66,77,88,99,111,112,113,115,118],1)
print(b)
