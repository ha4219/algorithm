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

t = int(stdin.readline().strip())


def find(x):
    if d[x] != x:
        d[x] = find(d[x])
    return d[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        d[y] = x


for p in range(t):
    n = int(stdin.readline().strip())
    m = dict()
    d = [int(i) for i in range(200001)]
    cnt = [0] * (200001)
    for _ in range(n):
        a, b = stdin.readline().split()
        res = 0
        ak = m.get(a)
        bk = m.get(b)
        if not ak:
            m[a] = len(m)
            res += 1
        if not bk:
            m[b] = len(m)
            res += 1
        res += cnt[find(m[a])]
        res += cnt[find(m[b])]
        union(m[a], m[b])
        cnt[find(m[a])] = res
        cnt[find(m[b])] = res
        print(cnt[find(m[a])])
