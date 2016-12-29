n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(',')]
new_arr = [None]*n
for item in arr:
    n -= 1
    new_arr[n] = item
new_arr = ' '.join(map(str,new_arr))
print(new_arr)
