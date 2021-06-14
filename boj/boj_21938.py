from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int,input().split())

a = [[0]*m for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

t = int(input())

for i in range(n):
    for j in range(m):
        s = (b[i][j*3]+b[i][j*3+1]+b[i][j*3+2])/3
        a[i][j] = 1 if s>=t else 0

v = [[0]*m for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def dfs(x,y):
    v[x][y] = 1
    for i in range(4):
        cx,cy=x+dx[i],y+dy[i]
        if cx<0 or cy<0 or cx>=n or cy>=m or v[cx][cy] or a[cx][cy]==0:
            continue
        dfs(cx,cy)
    return

res = 0
for i in range(n):
    for j in range(m):
        if v[i][j]==0 and a[i][j]==1:
            res += 1
            dfs(i,j)
print(res)