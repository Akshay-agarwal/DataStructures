def binarySearch(arr,key):

    low = 0;
    high = len(arr)-1

    if low > high:
        return -1


    mid = round((low+high)/2)

    while(low == high):
        if  arr[mid] == key:
            return "Element found at position: "+str(mid+1)

        elif(arr[mid] > key):
            high = mid
            mid = round((low+high)/2)


        else:
            low = mid
            mid = round((low+high)/2)


    return "Element no found"

b = binarySearch([1,2,3,4,5,6,7,8,9,11,14,16,17,19,25,26,65,74,85,88],95)
print(b)
