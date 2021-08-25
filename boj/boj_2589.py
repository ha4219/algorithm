from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(x,y):
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x,y,0))
    v[x][y] = 1
    res = 0
    while q:
        x, y, c = q.popleft()
        res = max(res, c)
        for i in range(4):
            cx, cy = x+dx[i],y+dy[i]
            if cx<0 or cy<0 or cx>=n or cy>=m or v[cx][cy] \
                or a[cx][cy]=='W':
                continue
            v[cx][cy] = 1
            q.append((cx,cy,c+1))
    return res

res = 0
for i in range(n):
    for j in range(m):
        if a[i][j]=='L':
            res = max(res, bfs(i,j))
print(res)