import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n, m = map(int, input().split())
aa = [input().split() for _ in range(n-1)]

def solve():
    pos = 1
    for i in range(n-1):
        a = aa[i]
        x = int(a[0])
        l, r = 0, m + 1

        for j in range(x):
            p, d = int(a[j*2 + 1]), a[j*2 + 2]
            if d == 'L': l = max(l, p)
            else: r = min(r, p)

        if x == 0: continue
        elif r <= pos and pos <= l:
            pos = l + 1
        elif l <= r:
            if pos <= l:
                pos = l + 1
            if r <= pos:
                pos = m + 1
    
    print("YES" if pos <= m else 'NO')
    return

solve()