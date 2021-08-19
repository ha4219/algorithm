from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)


# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]


# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x != y:
#         if x>y:
#             x, y = y, x
#         parent[y] = x


n = int(input())
a = [0] + list(map(int, input().split()))

m = int(input())
querys = [[] for _ in range(m+1)]
change_querys = []

for i in range(m):
    query = list(map(int, input().split()))
    if query[0]==1:
        change_querys.append((query[1], query[2]))
    else:
        querys[query[1]].append((i, query[2], query[3]))
s = [0] * (4*n+1)

# def q(i):
#     res = 0
#     while i>0:
#         res += s[i]
#         i &= (i-1)
#     return res

def q(l, r, node, nL, nR):
    if nL>r or nR<l:
        return 0
    if l<=nL and nR<=r:
        return s[node]
    m = (nL+nR)//2
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR)

def u(i, v, node, nL, nR):
    if nL>i or nR<i:
        return s[node]
    if nL==nR:
        s[node] = v
        return v
    m = (nL+nR)//2
    s[node]=u(i,v,node*2,nL,m)+u(i,v,node*2+1,m+1,nR)
    return s[node]

# def u(i, v):
#     while i<=n:
#         s[i] += v
#         i += (i & -i)

for i in range(1,n+1):
    u(i,a[i], 1, 1, n)

res = []
for idx, cq in enumerate(change_querys):
    i, v = cq
    for query in querys[idx]:
        ii, l, r = query
        res.append((ii, q(l,r,1,1,n)))
    u(i, v, 1, 1, n)
for query in querys[len(change_querys)]:
    ii, l, r = query
    res.append((ii, q(l, r, 1, 1, n)))
res.sort()
for a,b in res:
    print(b)