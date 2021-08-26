from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

MOD = 1000000
n = int(input())

res = [0] * (n+1)
res[1] = 1
for i in range(2, n+1):
    res[i] = (int(str(res[i-1]*i).replace('0', '')))%MOD
print(res[n])
