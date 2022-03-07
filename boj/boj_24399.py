from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 31623
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n, q, K = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
def select(p, r, q):
  if p==r:
    return a[p]
  t = partition(p, r)
  k = t - p + 1
  if q < k:
    return select(p, t-1, q)
  elif q == k:
    return a[t]
  return select(t+1,r,q-k)

def partition(p, r):
  global cnt
  x = a[r]
  i = p - 1
  for j in range(p, r):
    if a[j] <= x:
      i += 1
      a[i], a[j] = a[j], a[i]
      cnt += 1
      if cnt == K:
        print(*a)
        exit(0)
  if i + 1 != r:
    a[i+1], a[r] = a[r], a[i+1]
    cnt += 1
    if cnt == K:
      print(*a)
      exit(0)
  return i+1
select(0, n-1, q)

print(-1)