from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n = int(input())
a = []
for _ in range(n):
    p,q=input().split()
    a.append([p, int(q)])
d = [[-1]*(n+1) for _ in range(n+1)]

def f(l, r):
    if l==r:
        return 1 if a[l][0]=='y' else 0
    if d[l][r]!=-1:
        return d[l][r]
    if a[l][0]=='y' and a[r][0]=='y':
        nmax = 0
        cnt = 0
        for i in range(l, r+1):
            if a[i][0]=='n':
                nmax = max(nmax, a[i][1])
            else:
                cnt = 1
        flag = 1
        for i in range(l, r+1):
            if a[i][1]<nmax:
                flag = 0
                break
        if flag or nmax==0:
            d[l][r] = cnt
            return d[l][r]
    d[l][r] = maxsize
    for i in range(l, r):
        left = f(l, i)
        right = f(i+1, r)
        tmp = left+right
        d[l][r] = min(d[l][r], tmp)
    return d[l][r]

print(f(0,n-1))
