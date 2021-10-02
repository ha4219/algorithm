from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
tmp = 0
for num in a:
    tmp ^= num

res = tmp
for i in range(n):
    res = max(res, tmp^a[i])
print("%d%d"%(res,res))