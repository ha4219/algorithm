from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

d1 = [[-1]*m for _ in range(n)]
d2 = [[-1]*m for _ in range(n)]
dx,dy = (0,-1,0),(1,0,-1)

def dfs1(sx,sy):
    q = deque()
    q.append((sx,sy))
    d1[sx][sy] = a[sx][sy]
    while q:
        x,y=q.popleft()
        for i in range(2):
            cx,cy=x+dx[i],y+dy[i]
            if cx<0 or cy<0 or cx>=n or cy>=m:
                continue
            if d1[cx][cy]==-1:
                d1[cx][cy] = d1[x][y]+a[cx][cy]
                q.append((cx,cy))
            else:
                if d1[cx][cy]<d1[x][y]+a[cx][cy]:
                    d1[cx][cy] = d1[x][y]+a[cx][cy]
                    q.append((cx,cy))

def dfs2(sx,sy):
    q = deque()
    q.append((sx,sy))
    d2[sx][sy] = a[sx][sy]
    while q:
        x,y=q.popleft()
        for i in range(1,3):
            cx,cy=x+dx[i],y+dy[i]
            if cx<0 or cy<0 or cx>=n or cy>=m:
                continue
            if d2[cx][cy]==-1:
                d2[cx][cy] = d2[x][y]+a[cx][cy]
                q.append((cx,cy))
            else:
                if d2[cx][cy]<d2[x][y]+a[cx][cy]:
                    d2[cx][cy] = d2[x][y]+a[cx][cy]
                    q.append((cx,cy))


# print()
dfs1(n-1,0)
dfs2(n-1,m-1)
def pp(a):
    for i in a:
        print(*i)
# pp(d1)
# print()
# pp(d2)
res = -maxsize
for i in range(n):
    for j in range(m):
        res = max(res,d1[i][j]+d2[i][j])
print(res)