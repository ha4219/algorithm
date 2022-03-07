from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

a2, a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

d = a1 ** 2 + 4 * (c - a2) * a0

def f(x):
  return a2 * (x**2) + a1 * x + a0
def g(x):
  return c * (x ** 2)

if a2 == c:
  if a1 == a0 == 0:
    print(1)
  else:
    if a1 > 0: # f는 좌측
      print(0)
    elif a1 == 0: # f는 공중에 떠있음
      print(0)
    else: # f는 우측
      print(1)
elif a2 == 0:
  print(1 if f(n0) <= g(n0) else 0)
elif a2 > c:
  print(0)
elif d < 0: # 만나지 않음
  center = f(n0)
  right = g(n0)
  print(1 if center <= right else 0)
elif d == 0: # 한 점에서 만남
  xx = -a1 / (2 * (c - a2))
  center = f(n0)
  right = g(n0)
  print(1 if center <= right else 0)
else: # d > 0 즉 두 점에서 만남, 
  x = (a1 + d ** (1/2)) / (2 * (c - a2))
  # print(x)
  if a2 > 0: # 양수
    xx = a1 / (2 * (c - a2))
    if f(xx) < g(xx): # g가 위에 있음
      print(0)
    else:
      print(1 if n0 >= x else 0)
  else: # 음수
    print(1 if n0 >= x else 0)
  # x = x if x >= n0 else n0 
