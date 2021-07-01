from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *


input = stdin.readline
setrecursionlimit(10**6)



n, k = map(int,input().split())
a = [int(input()) for _ in range(n)]

l = 0
r = 1000000000000000000

res = 99999999999999
while l<=r:
    s = 0
    m = (l+r) // 2
    for i in range(n):
        s += m//a[i]
    if s>=k:
        res = m
        r = m - 1
    else:
        l = m + 1
print(res)