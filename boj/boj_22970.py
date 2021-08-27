from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n = int(input())

a = list(map(int, input().split()))

up = [1] * (n+1)
down = [1] * (n+1)

res = 0
for i in range(1, n):
    if a[i]>a[i-1]:
        up[i] = up[i-1] + 1
    if a[n-1-i]>a[n-i]:
        # print(n-1-i, n-i)
        down[n-1-i] = down[n-i] + 1

for i in range(n):
    res = max(res, up[i]+down[i]-1)
# print(down)
# print(up)
print(res)