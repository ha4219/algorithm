from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n, k = map(int, input().split())

s =[0] * (4*n)
lazy = [[0] *2 for _ in range(4*n)]

def propagation(node, nL, nR):
    if lazy[node]:
        if nL!=nR:
            s[node] += (nR-nL+1)*lazy[node][0]
        elif s[node]!=-1:
            p = int(sqrt(s[node]*2))
            val, cnt = lazy[node]
            if p*cnt+(cnt*(cnt+1))//2==val:
                s[node] += val
            else:
                s[node] = -1

        if nL!=nR:
            lazy[node*2][0] += lazy[node][0]
            lazy[node*2][1] += lazy[node][1]
            lazy[node*2+1][0] += lazy[node][0]
            lazy[node*2+1][1] += lazy[node][1]
        lazy[node] = [0, 0]

def update(l, r, v, node, nL, nR):
    propagation(node, nL, nR)
    if l > nR or r < nL:
        return
    if l<=nL and nR<=r:
        if nL!=nR:
            s[node] += (nR-nL+1)*v
        elif s[node]!=-1:
            p = int(sqrt(s[node]*2))
            if p+1==v:
                s[node] += v
            else:
                s[node] = -1
        if nL!=nR:
            lazy[node*2][0] += v
            lazy[node*2][1] += 1
            lazy[node*2+1][0] += v
            lazy[node*2+1][1] += 1
        return
    m = nL + nR
    m = m // 2
    update(l,r,v,node*2,nL,m)
    update(l,r,v,node*2+1,m+1,nR)
    s[node] = s[node*2] + s[node*2+1]
    return s[node]

def merge(l, r, node, nL, nR):
    propagation(node, nL, nR)
    if l > nR or r < nL:
        return 0
    if l <= nL and nR <= r:
        return s[node]
    m = nL + nR
    m = m // 2
    return merge(l,r,node*2,nL,m) + merge(l,r,node*2+1,m+1,nR)

for _ in range(int(input())):
    l, r, x = map(int,input().split())
    update(l, r, x, 1, 1, n)

RES = (k*(k+1))//2
res = 0
for i in range(1, n+1):
    tmp = merge(i,i,1,1,n)
    if RES==tmp:
        res += 1
print(res)