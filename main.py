from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, m, k = map(int, input().split())
NMAX = 101
MMAX = 1001
PMAX = 501

a = [list(map(int, input().split())) for _ in range(n)]

# d = [[[-1]*501 for _ in range(1001)] for __ in range(101)]

d = [[[-1] * (n*5+1) for _ in range(1002)] for __ in range(n+1)]

def dfs(idx, cpu, memory, priority):
    if cpu>1000:
        cpu = 1001
    if d[idx][cpu][priority]!=-1:
        return d[idx][cpu][priority]
    if n==idx:
        # print(cpu, memory, priority)
        return priority if cpu>=m and memory>=k else maxsize
    d[idx][cpu][priority] = maxsize
    # select
    d[idx][cpu][priority] = min(d[idx][cpu][priority], \
        dfs(idx+1, cpu+a[idx][0], memory+a[idx][1], priority + a[idx][2]))
    # pass
    d[idx][cpu][priority] = min(d[idx][cpu][priority], \
        dfs(idx+1, cpu, memory, priority))

    return d[idx][cpu][priority]
print(dfs(0,0,0,0))