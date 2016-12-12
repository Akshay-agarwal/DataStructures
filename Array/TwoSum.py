def pair_sum(arr,k):
    count = 0
    output = set()
    d = {}
    for i in range(len(arr)):
        if arr[i] in d:
            output.add((max(arr[i],k-arr[i]),min(arr[i],k-arr[i])))
            count = count+1
        else:
            d[k-arr[i]] = i
    return output

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
