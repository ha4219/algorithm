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
  a = list(map(int, input().split()))

  cnt = 0
  for i in range(n):
    idx = a[:n-i].index(max(a[:n-i]))
    if idx == n-i-1: continue
    a[idx], a[n-i-1] = a[n-i-1], a[idx]
    cnt += 1
    if cnt == k:
      print(a[idx], a[n-i-1])
      return
  print(-1)

solve()
