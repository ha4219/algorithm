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


for i in range(1, n+1):
    if not v[i]:
        dfs(i, 1)

cuts = []
for i in range(1, n+1):
    if c[i]:
        cuts.append(i)


print(len(cuts))
print(*cuts)
