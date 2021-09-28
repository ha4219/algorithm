from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd
from bisect import *


input = stdin.readline
setrecursionlimit(10**5)

MAX = 1000001
s = [[] for _ in range(4*MAX)]

def update(idx, x, node, nL, nR):
    if idx<nL or idx>nR:
        return
    s[node].append(x)
    if nL!=nR:
        m = (nL+nR)//2
        update(idx,x,node*2,nL,m)
        update(idx,x,node*2+1,m+1,nR)

def query(x, l, r, node, nL, nR):
    if l>nR or r<nL:
        return 0
    if l<=nL and nR<=r:
        return bisect_right(s[node], x)
    m = (nL+nR)//2
    return query(x,l,r,node*2,nL,m)+query(x,l,r,node*2+1,m+1,nR)

n, q = map(int, input().split())
a = list(map(int, input().split()))
for i, x in enumerate(a):
    update(i+1, x, 1, 1, n)

for i in range(MAX*4):
    s[i].sort()

for _ in range(q):
    i, j, k = map(int, input().split())
    l, r = map(int, (-1e9, 1e9))
    while l<=r:
        m = (l+r)//2
        if query(m,i,j,1,1,n)<k:
            l = m + 1
        else:
            r = m - 1
    print(l)