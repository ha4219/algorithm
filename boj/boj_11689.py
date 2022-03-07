from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 1000001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())

res = n

for i in range(2, MAX):
  if n % i == 0:
    res //= i
    res *= (i - 1)
  while n % i == 0:
    n //= i
if n != 1:
  res //= n
  res *= (n-1)
print(res)