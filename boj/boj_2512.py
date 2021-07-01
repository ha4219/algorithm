from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *


input = stdin.readline
setrecursionlimit(10**6)



n = int(input())
a = list(map(int, input().split()))
k = int(input())
l = 0
r = k
res = 0

while l<=r:
    s = 0
    m = (l+r) // 2
    t = 0
    for i in range(n):
        tmp = min(m, a[i])
        s += tmp
        t = max(t, tmp)
    #     print(l,m,r, t)
    # print(s)
    if s>k:
        r = m - 1
    else:
        res = t
        l = m + 1
print(res)