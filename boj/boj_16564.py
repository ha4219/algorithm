from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *


input = stdin.readline
setrecursionlimit(10**6)



n, k = map(int,input().split())
a = [int(input()) for _ in range(n)]
l = 0
r = 2000000000

while l<=r:
    m = (l+r)//2
    s = 0
    for i in range(n):
        s += max(m-a[i], 0)
    if s>k:
        r = m - 1
    else:
        res = m
        l = m + 1
print(res)