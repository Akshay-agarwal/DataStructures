def pair_sum(arr,k):

    seen = set()
    output = set()
    count = 0
    if len(arr) < 2:
        return "The array size should be atleast 2"

    else:
        for num in arr:
            if k-num not in seen:
                seen.add(num)

            else:
                output.add((max(num,k-num),min(num,k-num)))
                count += 1
    print('\n'.join(map(str,list(output))))
pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)

