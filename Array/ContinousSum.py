def large_cont_sum(arr):
    if (len(arr) == 0):
        return "Size of Array is greater than 1"

    else:
        current_sum = max_sum = arr[0]

        for num in arr[1:]:

            current_sum = max(current_sum+num,num)

            max_sum = max(current_sum,max_sum)
        return max_sum  
