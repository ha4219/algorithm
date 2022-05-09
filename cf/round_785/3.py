from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random
 
MAX = 40004
M = 502
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline


def f(n):
  r = 0
  while n > 0:
    r = r * 10 + n % 10
    n //= 10
  return r

def p(n):
  return f(n) == n

a = [0]
d = [[0] * M for _ in range(MAX)]
for i in range(1, 2*MAX):
  if p(i):
    a.append(i)

for i in range(1, M):
  d[0][i] = 1

for i in range(1, MAX):
  d[i][0] = 0
  for j in range(1, M):
    if a[j] <= i:
      d[i][j] = (d[i][j-1] + d[i-a[j]][j]) % MOD
    else:
      d[i][j] = d[i][j-1]

for _ in range(int(input())):
  n = int(input())
  print(d[n][M-1])