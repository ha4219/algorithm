from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *


input = stdin.readline
setrecursionlimit(10**6)



x, y = map(int, input().split())


t = (y*100//x)
l = 0
r = 1000000000*2
res = maxsize

if t>=99:
    print(-1)
    exit(1)
    
while l<=r:
    m = (l+r) // 2
    tt = ((m+y)*100//(m+x))
    if tt==t:
        l = m + 1
    else:
        res = min(res, m)
        r = m - 1
print(res)