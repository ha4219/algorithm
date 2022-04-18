import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 200000
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))

res = maxsize
ret = []
a.sort()

for i in range(n-2):
    l, r = i+1, n-1
    while l < r:
        v = a[i]+a[l]+a[r]
        if res > abs(v):
            res = abs(v)
            ret = [a[i], a[l], a[r]]
        if v < 0:
            l += 1
        else:
            r -= 1
print(*ret)
