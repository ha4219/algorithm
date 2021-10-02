from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

MAX = 100001

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    p,q,e,r = map(int, input().split())
    a[p].append((q,e,r))
    a[q].append((p,e,r))

def dijkstra():
    pq = [(0, 0, 1)]
    v = [[maxsize, maxsize] for _ in range(n+1)]
    v[1] = [0,0] 
    while pq:
        length, cost, cur = heappop(pq)
        for next, nLen, nCost in a[cur]:
            if v[next][0]>length+nLen:
                v[next] = [length+nLen, nCost]
                heappush(pq, (v[next][0], v[next][1], next))
            elif v[next][0]==length+nLen and v[next][1]>nCost:
                v[next][1] = nCost
                heappush(pq, (v[next][0], v[next][1], next))
    res = 0
    for i in range(1, n+1):
        if v[i][1]==maxsize: continue
        res += v[i][1]
    return res
print(dijkstra())