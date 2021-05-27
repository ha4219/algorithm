from sys import stdin, setrecursionlimit, maxsize
from math import ceil


setrecursionlimit(10**6)
input = stdin.readline

n,m=map(int,input().split())

l = r = -1

a = [list(map(int,input().split())) for _ in range(n)]
a.sort()
res = 0
for i in range(n):
    if r<=a[i][0]:
        res += ceil((r-l)/m)
        # print(res, a[i],r,l)
        l = a[i][0]
        r = a[i][1]
    else:
        r = max(r, a[i][1])
    r = ceil((r-l)/m)*m+l

res += ceil((r-l)/m)
print(res)