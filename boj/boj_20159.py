from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

res = 0
odd = [0] * (n+2)
even = [0] * (n+2)

for i in range(n):
    if i%2:
        odd[i+1] = a[i] + odd[i-1]
        even[i+1] = even[i-1]
    else:
        odd[i+1] = odd[i-1]
        even[i+1] = a[i] + even[i-1]

res = max(odd[n], even[n])

for i in range(1,n):
    res = max(res, odd[i-1]+even[n-1]-even[i] + a[i-1])
print(res)