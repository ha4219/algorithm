from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

target = 10
n = 1000

def func(m):
	return True if m<=target else False

l = 0
r = n
res = -1
while l <= r:
    m = (l + r) // 2
    if func(m):
        res = m
        l = m + 1
    else:
        r = m - 1

print(res)
