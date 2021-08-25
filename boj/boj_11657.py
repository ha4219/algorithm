from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline

n, m = map(int, input().split())
a = []
d = [maxsize] * (n+1)

for _ in range(m):
    p,q,r = map(int, input().split())
    a.append((p,q,r))

def bellmanFord(start):
    d[start] = 0
    for i in range(n):
        for cur,next,time in a:
            if d[cur]!=maxsize and d[next]>d[cur]+time:
                d[next] = d[cur] + time
                if i == n-1:
                    return 1
    return 0

cycle = bellmanFord(1)
if cycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(-1 if d[i]==maxsize else d[i])