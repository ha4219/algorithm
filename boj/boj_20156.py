from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 100005

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

n, m, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
v = [0] * MAX
p = [0]
for _ in range(m):
    p.append(int(input()))
# if m!=0:
#     p = [0] + list(map(int, input().split()))

parent = [i for i in range(MAX)]

# check not union set
for i in range(1, m+1):
    v[p[i]] += 1
for i in range(1, n+1):
    if v[i]>0 or a[i]==-1:
        continue
    union(i, a[i])

querys = [[] for _ in range(MAX)]
for i in range(k):
    query = list(map(int, input().split()))
    querys[query[0]].append((i, query[1], query[2]))

res = []

for mm in range(m, -1, -1):
    for idx, x, y in querys[mm]:
        res.append((idx, find(x)==find(y)))
    
    if mm>0:
        if v[p[mm]] == 1:
            union(p[mm], a[p[mm]])
        else:
            v[p[mm]] -= 1
res.sort()
for a,b in res:
    print('Same Same;' if b else 'No;')