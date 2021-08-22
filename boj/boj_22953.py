from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, k, c = map(int, input().split())
a = list(map(int, input().split()))

def backtracking(idx, cc, time):
    res = 0
    if idx==n:
        for i in range(n):
            res += time//a[i]
        return res
    for i in range(idx, n):
        if cc<c and a[i]>1:
            cc += 1
            a[i] -= 1
            res = max(res, backtracking(i, cc, time))
            a[i] += 1
            cc -= 1
    res = max(res, backtracking(n, cc, time))
    return res

def f(time):
    res = backtracking(0,0,time)
    return res>=k

def solve():
    l = 0
    r = int(2e12+1)
    res = maxsize
    while l<=r:
        m = (l+r)//2
        tmp = f(m)
        if tmp:
            r = m - 1
            res = min(res, m)
        else:
            l = m + 1
    return res

print(solve())