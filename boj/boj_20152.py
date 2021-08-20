from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 31

d = [[0] * MAX for _ in range(MAX)]
h, n = map(int, input().split())

if h>n:
    h,n = n,h

d[h][h] = 1
for i in range(h, n+1):
    for j in range(h, n+1):
        if i<j:
            continue
        if i==0 and j==0:
            continue
        elif i==0:
            d[i][j] += d[i][j-1]
        elif j==0:
            d[i][j] += d[i-1][j]
        else:
            d[i][j] += d[i-1][j] + d[i][j-1]
print(d[n][n])