from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, k, c = map(int, input().split())
a = list(map(int, input().split()))

def f(time):

    return 1

def solve():
    l = 1
    r = int(1e12+1)
    res = maxsize
    while l<=r:
        m = (l+r)//2

        if f(m):
            r = m - 1
            res = min(res, m)
        else:
            l = m + 1
    return res
    
print(solve())