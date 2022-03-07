from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
d1 = [[0] * (n+1) for _ in range(n+1)]
d2 = [[0] * (n+1) for _ in range(n+1)]

d1[0][0] = a[0][0]
for i in range(r):
  for j in range(c):
    val = 0
    if i != 0:
      val = max(d1[i-1][j], val)
    if j != 0:
      val = max(d1[i][j-1], val)
    d1[i][j] = a[i][j] + val
for i in range(r-1, n):
  for j in range(c-1 ,n):
    val = 0
    if i != 0:
      val = max(d1[i-1][j], val)
    if j != 0:
      val = max(d1[i][j-1], val)
    d1[i][j] = a[i][j] + val

d2[0][0] = a[0][0]
for i in range(n):
  for j in range(n):
    val = 0
    if i != 0:
      val = max(d2[i-1][j], val)
    if j != 0:
      val = max(d2[i][j-1], val)
    if i == r-1 and j == c-1: continue
    d2[i][j] = a[i][j] + val if val != 0 or (i==0 and j==0) else 0

print(d1[n-1][n-1], d2[n-1][n-1])
# for i in d2:
#   print(i)