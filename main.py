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
    return parent[x]

def union(x, y):
    ori_x = x
    x = find(x)
    y = find(y)
    if x!=y:
        if x==ori_x:
            cycle[x] = 1
        parent[y] = x

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
    if v[i]:
        continue
    union(i, a[i])
res = []
for i in range(idx, -1, -1):
    print(parent, cycle)
    for j in querys[i]:
        tmp = find(j)
        res.append('CIKLUS' if cycle[tmp] else tmp)
    
    if i==0:
        continue
    x = joint.pop()
    union(x, a[x])
print(res)
print(parent)
print(cycle)