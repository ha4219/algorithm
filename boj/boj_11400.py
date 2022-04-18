from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 200000
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline


'''
3
4 1
5 1 + 2 = 3
6 1 + 2 + 3 = 6
7 1 + 2 + 3 + 4 = 10

res = 3 * 6 * 10 = 180
'''

n, m = map(int, input().split())
v = [0] * (n+1)
c = [0] * (n+1)

a = [[] for _ in range(n+1)]

vn = 0
cuts = []

for _ in range(m):
    p, q = map(int, input().split())
    a[p].append(q)
    a[q].append(p)


def dfs(cur, root):
    global vn
    vn += 1
    v[cur] = vn
    ret = vn
    child = 0

    for next in a[cur]:
        if v[next]:
            ret = min(ret, v[next])
            continue

        child += 1
        prev = dfs(next, 0)

        if not root and prev >= v[cur]:
            c[cur] = 1

        ret = min(ret, prev)

    if root:
        c[cur] = (child >= 2)

    return ret


def dfsf(cur, prev):
    global vn
    vn += 1
    v[cur] = vn
    ret = v[cur]

    for next in a[cur]:
        if next == prev:
            continue

        if v[next]:
            ret = min(ret, v[next])
            continue

        pprev = dfsf(next, cur)

        if pprev > v[cur]:
            cuts.append((min(cur, next), max(cur, next)))

        ret = min(ret, pprev)
    return ret


for i in range(1, n+1):
    if not v[i]:
        dfsf(i, 1)

cuts.sort()


print(len(cuts))
for cut in cuts:
    print(*cut)
