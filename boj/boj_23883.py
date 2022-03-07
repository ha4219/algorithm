from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

def solve():
  n, k = map(int, input().split())
  aa = list(map(int, input().split()))
  a = sorted(aa, reverse=True)

  dv = {}
  di = {}
  for i, v in enumerate(aa):
    dv[v] = i # value -> index
    di[i] = v # index -> value

  cnt = 0
  # print(di, dv)
  for i, v in enumerate(a):
    if dv[v] == n-i-1: continue
    cnt += 1
    l, r = di[n-1-i], v
    dv[l], dv[r] = dv[r], dv[l]
    di[dv[l]], di[dv[r]] = di[dv[r]], di[dv[l]]

    if cnt == k:
      print(di[dv[l]], di[dv[r]])
      return
  print(-1)

solve()