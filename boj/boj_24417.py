from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline
n = int(input())
m = {}
m[0] = 0
m[1] = 1
m[2] = 1
m[3] = 2

def f(n):
  tmp = m.get(n)
  if tmp: return tmp
  if n&1:
    tmp1 = f((n+1)//2)
    tmp2 = f((n+1)//2 - 1)
    res = ((tmp1*tmp1)%MOD + (tmp2*tmp2)%MOD)%MOD
  else:
    tmp1 = f((n)//2)
    tmp2 = f((n)//2 - 1)
    res = (tmp1*((tmp1+2*tmp2)%MOD))%MOD
  m[n] = res
  return res
print(f'{f(n)} {n-2 if n>2 else 1}')