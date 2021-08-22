from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 100005

n = int(input())
a = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]
cycle = [0] * (n+1)
v = [0] * (n+1)

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    if cycle[x]:
        cycle[parent[x]] = 1
    return parent[x]

def union(x, y):
    ori_x = x
    ori_y = y
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x] = y
    else:
        if ori_x!=ori_y:
            for i in range(n+1):
                if parent[i]==x or parent[i]==y:
                    cycle[i] = 1
    if cycle[ori_x]!=cycle[ori_y]:
        cycle[ori_x] = 1
        cycle[ori_y] = 1


q = int(input())
querys = [[] for _ in range(q+1)]
joint = []
idx = 0
for i in range(q):
    p, q = map(int, input().split())
    if p==1:
        querys[idx].append(q)
    else:
        joint.append(q)
        v[q] = 1
        idx += 1
for i in range(1, n+1):
    if v[i] or a[i]==0:
        continue
    union(i, a[i])
res = []
for i in range(idx, -1, -1):
    # print(parent, cycle)
    for j in querys[i]:
        tmp = find(j)
        res.append('CIKLUS' if cycle[tmp] else tmp)
    
    if i==0:
        continue
    x = joint.pop()
    union(x, a[x])

res.reverse()
for i in res:
    print(i)