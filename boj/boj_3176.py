from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

for ____ in range(int(input())):
    n = int(input())

    a = [[] for _ in range(n+1)]
    v = [0] * (n+1)

    parent = [[[0, maxsize, -maxsize]
               for __ in range(MAX+1)] for _ in range(n+1)]
    d = [0] * (n+1)

    for _ in range(n-1):
        p, q = map(int, input().split())
        v[q] = 1
        a[p].append(q)

    p = 0
    for i in range(1, n+1):
        if v[i] == 0:
            p = i
            break

    def dfs(cur, depth):
        for next in a[cur]:
            if d[next]:
                continue
            parent[next][0][0] = cur
            d[next] = depth + 1
            dfs(next, depth+1)
        return

    d[p] = 0
    dfs(p, 0)

    for i in range(1, MAX):
        for j in range(1, n+1):
            parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]

    def solve(l, r):
        if d[l] > d[r]:
            l, r = r, l
        for i in range(MAX, -1, -1):
            if d[r] - d[l] >= (1 << i):
                left = parent[r][i][1]
                r = parent[r][i][0]
        if l == r:
            return l
        for i in range(MAX, -1, -1):
            if parent[l][i][0] != parent[r][i][0]:
                l = parent[l][i][0]
                r = parent[r][i][0]
        return parent[l][0][0]

    p, q = map(int, input().split())
    print(solve(p, q))
