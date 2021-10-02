from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x>y:
            x, y = y, x
        parent[y] = x


n, q = map(int, input().split())
parent = [i for i in range(n+1)]

prev = [0] * (n+1)
for i in range(2, n+1):
    tmp = int(input())
    prev[i] = tmp

res = []
querys = [list(map(int, input().split())) for __ in range(q+n-1)]
querys.reverse()
for query in querys:
    if query[0]==0:
        _, p1 = query
        union(p1, prev[p1])
    else:
        _, p1, p2 = query
        res.append(find(p1)==find(p2))
res.reverse()
for i in res:
    if i:
        print('YES')
    else:
        print('NO')
