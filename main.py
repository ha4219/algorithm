from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd
from bisect import *

input = stdin.readline
setrecursionlimit(10**5)

# n = int(input())
# start = list(map(int, input().split()))

# dx, dy = (2, 2, 1, 1, -1, -1, -2, -2), (-1, 1, -2, 2, -2, 2, -1, 1)

# def dfs(x, y):
#     return

a = [8,18,15,10,7,14]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    print(lesser_arr, equal_arr, greater_arr)
    print(lesser_arr+equal_arr+greater_arr)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
print(quick_sort(a))