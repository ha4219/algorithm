from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n = int(input())

a = list(map(int, input().split()))

s = [0] * (4*n)

def u(i, v, node, nL, nR):
    if i<nL or i>nR:
        return s[node]
    if nL==nR:
        s[node] = v
        return s[node]
    m = (nL+nR)//2
    s[node] = u(i,v,node*2,nL,m)+u(i,v,node*2+1,m+1,nR)
    return s[node]

def q(l, r, node, nL, nR):
    if l>nR or r<nL:
        return 0
    if l<=nL and nR<=r:
        return s[node]
    m = (nL+nR)//2
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR)

for i, num in enumerate(a):
    u(i,num,1,0,n-1)
for _ in range(int(input())):
    l,r = map(int, input().split())
    print(q(l-1,r-1,1,0,n-1))