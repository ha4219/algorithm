from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *


input = stdin.readline
setrecursionlimit(10**6)



n = int(input())
m = int(input())
a = list(map(int,input().split()))

l = 0
r = n
res = maxsize


while l<=r:
    mid = (l+r) // 2
    c = 1
    if a[0] - mid>0:
        c = 0
    for i in range(1,m):
        if a[i-1]+mid<a[i]-mid or c==0:
            c = 0
            break
    if a[m-1]+mid<n:
        c = 0
    if c:
        res = min(res, mid)
        r = mid-1
    else:
        l = mid+1
print(res)
    