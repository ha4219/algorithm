from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
p = list(map(int, input().split()))
res = 0
for i in p:
    res ^= i
print('koosaga' if res else 'cubelover')