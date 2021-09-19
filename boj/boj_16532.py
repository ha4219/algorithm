from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

MAX = 100001

s = [0] * (4*MAX)

def init(node, nL, nR):
    if nL==nR:
        s[node] = 1
        return s[node]
    m = (nL+nR)//2
    s[node] = init(node*2, nL, m) + init(node*2+1, m+1, nR)
    return s[node]

def update(i, v, node, nL, nR):
    if i<nL or i>nR:
        return s[node]
    if nL==nR:
        s[node] = v
        return s[node]
    m = (nL+nR)//2
    s[node] = update(i,v,node*2,nL,m)+update(i,v,node*2+1,m+1,nR)
    return s[node]

def query(l,r,node,nL,nR):
    if l>nR or r<nL:
        return 0
    if l<=nL and nR<=r:
        return s[node]
    m = (nL+nR)//2
    return query(l,r,node*2,nL,m)+query(l,r,node*2+1,m+1,nR)

q = int(input())
prime = []
primeCheck = [1] * MAX
check = [0] * MAX
qs = []
for i in range(q):
    n,k=map(int, input().split())
    qs.append((k, n, i))
qs.sort(reverse=True)

for i in range(2, MAX):
    if not primeCheck[i]:
        continue
    prime.append(i)
    for j in range(i*2, MAX, i):
        primeCheck[j] = 0
init(1, 1, MAX-1)
idx = len(prime) - 1
res = [0] * q
for k, n, i in qs:
    while idx>-1:
        if prime[idx]<=k:
            break
        for j in range(prime[idx], MAX, prime[idx]):
            if check[j]:
                continue
            check[j] = 1
            update(j, 0, 1, 1, MAX-1)
        idx -= 1
    res[i] = query(2, n, 1, 1, MAX-1)
for re in res:
    print(re)