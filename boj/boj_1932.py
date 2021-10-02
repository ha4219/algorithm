from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1]*(n+1) for _ in range(n+1)]

d[0][0] = a[0][0]
for i in range(n-1):
    for j in range(i+1):
        d[i+1][j] = max(d[i+1][j], d[i][j]+a[i+1][j])
        d[i+1][j+1] = max(d[i+1][j+1], d[i][j]+a[i+1][j+1])
print(max(d[n-1]))
