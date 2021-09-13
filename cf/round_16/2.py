from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd, ceil


input = stdin.readline
setrecursionlimit(10**5)

def mex(s):
    fl = 0
    for c in s:
        if c=='0':
            fl |= 1
        elif c=='1':
            fl |= 2
    if fl==3:
        return 2
    if fl==1:
        return 1
    return 0

def solution(n, s1, s2):
    d = [0] * (n+1)
    for i in range(n):
        s = ''
        for j in range(n):
            if i+j>=n: break
            s += s1[i+j]
            s += s2[i+j]
            d[i+j+1] = max(d[i+j+1], d[i]+mex(s))
    return d[n]

for _ in range(int(input())):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    print(solution(n, s1, s2))