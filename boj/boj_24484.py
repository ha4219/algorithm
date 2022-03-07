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
  a[i].sort(reverse=True)

res = [-1] * (n+1)
cnt = [0] * (n+1)

c = 0
def dfs(cur, dep):
  global c
  c += 1
  v[cur]=1
  cnt[cur] = c
  res[cur] = dep
  for next in a[cur]:
    if v[next]: continue
    dfs(next, dep+1)
  return

dfs(r, 0)
# print('\n'.join(map(str, res[1:])))
print(sum([res[i]*cnt[i] for i in range(1, n+1)]))