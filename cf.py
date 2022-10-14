from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

for _ in range(int(input())):
  s = input().strip()
  sl = len(s)
  res = {}
  k = 0
  ret = 1
  for i, c in enumerate(s):
    tmp = res.get(c)
    if tmp:
      # print(tmp, c)
      k = i
      break
    else:
      res[c] = 1

  for i in range(k, sl):
    if s[i] != s[i-k]:
      ret = 0
      break
  print('YES' if ret else 'NO')


# 비둘기 집
# 구현인데 왜 못함~