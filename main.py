from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int,input().split())


a = [[] for _ in range(n+1)]

for _ in range(m):
    p,q=map(int,input().split())
    a[q].append(p)

res = 0
v = [0] * (n+1)
def dfs(idx):
    global res
    v[idx] = 1
    for next in a[idx]:
        if v[next]:
            continue
        res += 1
        dfs(next)

dfs(int(input()))
print(res)