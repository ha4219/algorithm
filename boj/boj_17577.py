from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

while 1:
    n, m = map(int, input().split())
    if n==0:
        break
    a = [list(map(int, input().split())) for _ in range(m)]

    res = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[j][i]
        res = max(res, tmp)
    print(res)