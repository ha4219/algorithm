from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from itertools import combinations
from collections import deque
import random
import math

MAX = 17
MOD = 1000000000007
MOD2 = MOD * 2
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())
d = {}

a = [int(input()) for _ in range(n)]
a.sort()

for key in a:
    val = d.get(key)
    if val:
        d[key] += 1
    else:
        d[key] = 1

dd = []
dv = 0

for key in d.keys():
    if dv == d[key]:
        dd.append(key)
    elif dv < d[key]:
        dv = d[key]
        dd = [key]

dd.sort()

print('%d' % round(sum(a) / n, 0))
print(a[n//2])

print(dd[1] if len(dd) > 1 else dd[0])
print(a[n-1] - a[0])
