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
dis = [0] * (n+1)
v = [0] * (n+1)

for _ in range(n-1):
    p, q, c = map(int, input().split())
    a[p].append((q, c))
    a[q].append((p, c))


def dfs(cur, depth, distance):
    if v[cur]:
        return

    for next, next_cost in a[cur]:
        if d[next] != 0:
            continue
        parent[next][0] = cur
        dis[next] = distance + next_cost
        d[next] = depth+1
        dfs(next, depth+1, dis[next])
    return


dfs(1, 1, 0)


for i in range(1, MAX):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

cache = {}


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
for _ in range(m):
    p, q = map(int, input().split())
    ancestor = solve(p, q)
    print(dis[p] + dis[q] - dis[ancestor] * 2)
