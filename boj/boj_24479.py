from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n, m, r = map(int, input().split())
a = [[] for _ in range(n+1)]

for _ in range(m):
  p, q = map(int, input().split())
  a[p].append(q)
  a[q].append(p)

v = [0] * (n+1)
for i in range(1, n+1):
  a[i].sort()

cnt = 0
res = [0] * (n+1)
def dfs(cur):
  global cnt
  cnt += 1
  v[cur]=1
  res[cur] = cnt
  for next in a[cur]:
    if v[next]: continue
    dfs(next)
  return

dfs(r)
print('\n'.join(map(str, res[1:])))