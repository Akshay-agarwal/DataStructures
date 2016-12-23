def BsRec(arr,key,low,high):
    if low > high:
        return "Key not found"

    else:
        mid = (low+high)//2
        if arr[mid] == key:
            return "Key found at "+str(mid+1)

        elif arr[mid]<key:
            return BsRec(arr,key,mid+1,high)

        else:
            return BsRec(arr,key,low,mid-1)

def Bs(arr,key):
    return BsRec(arr,key,0,len(arr)-1)

print(Bs([1,2,3,4,6,8,9,11,12,34,55,66,77,88,91,92,94,99,111,112,113,115,118,1192,13233,34546,6575676],10))

