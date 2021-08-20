from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))

res = [0] * (n+1)
for i in a:
    res[i] += 1
print(max(res))