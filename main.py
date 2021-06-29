from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *


input = stdin.readline
setrecursionlimit(10**6)


n, m = map(int,input().split())
a = [int(input()) for _ in range(n)]

l = 0
r = sum(a)*2
res = maxsize

def f(mon):
    cur = 0
    cnt = 0
    for i in range(n):
        if a[i] > mon:
            return 0
        if cur<a[i]:
            cur = mon
            cnt += 1
        cur -= a[i]
    return cnt<=m

while l<=r:
    mid = (l+r)//2
    # print(l,r,mid)
    if f(mid):
        res = min(res, mid)
        r = mid - 1
    else:
        l = mid + 1
print(res)