#!/bin/python3

import sys

size, n = map(int, input().strip().split())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
new_arr = []*size

while n > 0:
    for i in range(len(arr)-1):
        new_arr[i] = arr[i-1]
    n -= 1
    arr = new_arr

print(new_arr)
