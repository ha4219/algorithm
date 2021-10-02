from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n = int(input())

for i in range(1, n+1):
    a = list(map(int, input().split()))
    a = a[1:]
    a.sort()
    print("Class %d"%i)
    res = 0
    l = len(a)
    for i in range(l-1):
        res = max(res, a[i+1]-a[i])
    print("Max %d, Min %d, Largest gap %d"%(a[-1],a[0],res))