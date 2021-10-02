from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
a, b, c, m = map(int, input().split())

p = 0
res = 0

for _ in range(24):
    if p+a<=m:
        p += a
        res += b
    elif p-c>=0:
        p -= c
print(res)