from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = [int(input()) for _ in range(n)]

d = [0] * (n+1)

d[0] = a[0]

for i in range(1, n):
    d[i] = a[i]
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + a[i])
print(max(d))