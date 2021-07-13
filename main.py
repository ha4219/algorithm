from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt


input = stdin.readline
setrecursionlimit(10**6)


n = int(input())
a = [[] for _ in range(n+1)]
for _ in range(n-1):
    p,q=map(int,input().split())
    a[p].append(q)
    a[q].append(p)

d = g = 0
for i in range(1,n+1):
    if len(a[i])==3:
        g += 1
    