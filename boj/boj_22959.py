from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

s = [0] * (n*4)

def init(node, nL, nR):
    if nL==nR:
        s[node] = a[nL]
        return s[node]
    m = (nL+nR)//2
    s[node] = max(init(node*2,nL,m), init(node*2+1,m+1,nR))
    return s[node]

def u(i, v, node, nL, nR):
    if i>nL or nR<i:
        return s[node]
    if nL==nR:
        a[i] = v
        s[node] = a[i]
        return s[node]
    m = (nL+nR)//2
    s[node] = max(u(i,v,node*2,nL,m), u(i,v,node*2+1,m+1,nR))
    return s[node]

def q(l, r, node, nL, nR):
    if l>nR or nL>r:
        return 0
    if l<=nL and nR<=r:
        return s[node]
    m = (nL+nR)//2
    return max(q(l,r,node*2,nL,m), q(l,r,node*2+1,m+1,nR))

init(1,0,n-1)
for _ in range(int(input())):
    p = list(map(int, input().split()))
    if p[0]==1:
        u(p[1]-1, p[2], 1, 0, n-1)
    else:
        print(q(p[1], p[2], 1, 0, n-1))