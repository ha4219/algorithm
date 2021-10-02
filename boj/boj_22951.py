from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, k = map(int, input().split())
a = []
for i in range(n):
    t = list(map(int, input().split()))
    for tt in t:
        a.append((tt, i+1))
total = n*k

idx = 0
while total>1:
    tmp = a.pop(idx)
    total -= 1
    idx = (idx+tmp[0]-1) % total
print(a[0][1], a[0][0])