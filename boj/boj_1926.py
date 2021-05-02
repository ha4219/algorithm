from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline

n,m=map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def dfs(x,y):
    v[x][y] = 1
    c = 1
    for i in range(4):
        cx, cy = x+dx[i],y+dy[i]
        if cx<0 or cx>=n or cy<0 or cy>=m or v[cx][cy] or a[cx][cy]==0:
            continue
        v[cx][cy]
        c += dfs(cx, cy)
    return c

res = 0
rec = 0
for i in range(n):
    for j in range(m):
        if v[i][j] or a[i][j]==0:
            continue
        c = dfs(i,j)
        rec += 1
        res = max(res, c)
print(rec)
print(res)