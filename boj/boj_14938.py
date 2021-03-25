from sys import stdin
from heapq import *

input = stdin.readline
maxsize = 10**6
n,m,r=map(int,input().split())
d = [[maxsize]*n for _ in range(n)]
t = list(map(int,input().split()))

for i in range(r):
    a,b,c=map(int,input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][k]+d[k][j],d[i][j])


def go(start):
    res = t[start]
    for i in range(n):
        if i==start:
            continue
        if m>=d[start][i]:
            res += t[i]
    return res

res = 0
for i in range(n):
    res = max(go(i),res)
print(res)