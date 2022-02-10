from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
setrecursionlimit(10**5)
input = stdin.readline

q = deque()
n, m, r = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
  u, v = map(int, input().split())
  a[u].append(v)
  a[v].append(u)
  
for i in range(1, n+1):
  a[i].sort()

v = [0] * (n+1)
t = [0] * (n+1)
d = [-1] * (n+1)

i = 1
q.append(r)
v[r] = 1
dep = 0
while q:
  for _ in range(len(q)):
    cur = q.popleft()
    d[cur] = dep
    t[cur] = i
    i += 1
    for next in a[cur]:
      if v[next]: continue
      v[next] = 1
      q.append(next)
  dep += 1

res = 0
for i in range(1, n+1):
    res += t[i] * d[i]
print(res)
