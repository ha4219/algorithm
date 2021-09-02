from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

MAX = 50000
d = []
for i in range(int(sqrt(MAX)+1)):
    d.append(i*i)

n = int(input())
l = len(d)
dp = [maxsize] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    idx = 1
    while idx<l and i>=d[idx]:
        dp[i] = min(dp[i], dp[i-d[idx]]+1)
        idx += 1
print(dp[n])
