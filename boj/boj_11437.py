from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 999
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())

a = [[] for _ in range(n+1)]
parent = [0] * (n+1)
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
    parent[cur] = prev
    d[cur] = depth
    for next in a[cur]:
        if v[next]:
            continue
        dfs(cur, next, depth+1)
    return


dfs(0, 1, 1)


def solve(l, r):
    if d[l] > d[r]:
        l, r = r, l
    if l == r:
        return l
    if l == 1 or r == 1:
        return 1
    if d[l] == d[r]:
        return solve(parent[l], parent[r])
    return solve(l, parent[r])


m = int(input())
for _ in range(m):
    p, q = map(int, input().split())
    print(solve(p, q))
# print(parent)
# print(d)
