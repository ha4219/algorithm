from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

res = 0
left = 0
right = 0

# ? 

# 정직
for i in range(n):
    if i%2:
        left += a[i]
    else:
        right += a[i]
res = max(left, right)
