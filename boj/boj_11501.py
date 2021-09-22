from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

MAX = 100001

def solve(n, a):
    res = 0
    ma = [0] * n
    ma[n-1] = a[n-1]
    for i in range(1, n):
        ma[n-i-1] = max(a[n-i-1], ma[n-i])
    for i in range(n):
        res += ma[i]-a[i]
    print(res)
    return 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)