from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
setrecursionlimit(10**5)
input = stdin.readline

f = [0] * 41
f[1] = f[2] = 1
n = int(input())
for i in range(3, 41):
  f[i] = f[i-1] + f[i-2]
print(f'{f[n]} {n-2 if n>2 else 1}')