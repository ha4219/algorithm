from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)


n = int(input())
d = [0] * (n+1)
for i in range(n+1):
    d[i] = int(str(i), 11)

