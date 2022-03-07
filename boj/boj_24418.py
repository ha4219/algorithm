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
c = [[0] * (31) for _ in range(31)]
c[0][0] = c[0][1] = c[1][0] = c[1][1] = 1

for j in range(1, 2*n+1):
  for i in range(j+1):
    if i==0 or i==j:
      c[j][i] = 1
    else:
      c[j][i] = c[j-1][i-1] + c[j-1][i]

print(c[2*n][n], n*n)