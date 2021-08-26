from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

a,b,n,w = map(int, input().split())

res = []
for i in range(1, n):
    if a*i+b*(n-i)==w:
        res.append((i, n-i))

if len(res)==1:
    print(*res[0])
else:
    print(-1)
    