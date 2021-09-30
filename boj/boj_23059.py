from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd
from bisect import *

input = stdin.readline
setrecursionlimit(10**5)
MAX = 400001

n = int(input().strip())
d = {}
rd = {}
depth = [0] * MAX
a = [[] for _ in range(MAX)]

for _ in range(n):
    p, q = input().split()
    if not d.get(p):
        d[p] = len(d)+1
        rd[d[p]] = p
    if not d.get(q):
        d[q] = len(d)+1
        rd[d[q]] = q
    p = d.get(p)
    q = d.get(q)
    depth[q] += 1
    a[p].append(q)

q = deque()
for i in range(1, len(d)+1):
    if depth[i]==0:
        q.append((rd[i], i))

cnt = 0
res = []
while q:
    q = deque(sorted(q))
    for __ in range(len(q)):
        _, cur = q.popleft()
        cnt += 1
        res.append(rd[cur])
        for next in a[cur]:
            depth[next] -= 1
            if depth[next]==0:
                q.append((rd[next], next))
print('\n'.join(map(str,res)) if len(res)==len(d) else -1)