from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 27
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())
a = []
for _ in range(n):
    p, q = map(int, input().split())
    if p < q:
        a.append([p, q])
    else:
        a.append([q, p])
a.sort(key=lambda x: x[1])
d = int(input())

pq = []
res = 0
for item in a:
    if item[1] - item[0] > d:
        continue
    while pq and item[1] - d > pq[0][0]:
        heappop(pq)
    heappush(pq, item)
    res = max(res, len(pq))
print(res)
