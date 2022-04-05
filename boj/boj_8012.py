from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())

a = [[] for _ in range(n+1)]
parent = [[0] * (MAX+1) for _ in range(n+1)]
d = [0] * (n+1)
v = [0] * (n+1)

for _ in range(n-1):
    p, q = map(int, input().split())
    a[p].append(q)
    a[q].append(p)


def dfs(prev, cur, depth):
    if v[cur]:
        return
    v[cur] = 1
    parent[cur][0] = prev
    d[cur] = depth
    for next in a[cur]:
        if v[next]:
            continue
        dfs(cur, next, depth+1)
    return


dfs(0, 1, 1)


for i in range(1, MAX):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]



def solve(l, r):
    if d[l] > d[r]:
        l, r = r, l
    for i in range(MAX, -1, -1):
        if d[r] - d[l] >= (1 << i):
            r = parent[r][i]
    if l == r:
        return l
    for i in range(MAX, -1, -1):
        if parent[l][i] != parent[r][i]:
            l = parent[l][i]
            r = parent[r][i]
    return parent[l][0]


m = int(input())
ms = [int(input()) for _ in range(m)]

res = 0
for i in range(m-1):
    res += -d[solve(ms[i], ms[i+1])] * 2 + d[ms[i]] + d[ms[i+1]]
print(res) 