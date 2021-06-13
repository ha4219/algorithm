from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

q = deque()
v = [[[0]*4 for _ in range(m)] for _ in range(n)]
r = [0]*(n*m)
for i in range(n):
    for j in range(m):
        if a[i][j]==9:
            r[i*m+j] = 1
            for k in range(4):
                q.append((i,j,k))
                v[i][j] = [1,1,1,1]

dx,dy=(0,0,1,-1),(1,-1,0,0)
def bfs():
    while q:
        x,y,d = q.popleft()
        cx,cy = x+dx[d],y+dy[d]
        if cx<0 or cy<0 or cx>=n or cy>=m or v[cx][cy][d]:
            continue
        v[cx][cy][d] = 1
        r[cx*m+cy] = 1
        if a[cx][cy]==0:
            q.append((cx,cy,d))
        elif a[cx][cy]==1:
            if d>1:
                q.append((cx,cy,d))
        elif a[cx][cy]==2:
            if d<2:
                q.append((cx,cy,d))
        elif a[cx][cy]==3:
            if d==0:
                q.append((cx,cy,3))
            elif d==1:
                q.append((cx,cy,2))
            elif d==2:
                q.append((cx,cy,1))
            else:
                q.append((cx,cy,0))
        else:
            if d==0:
                q.append((cx,cy,2))
            elif d==1:
                q.append((cx,cy,3))
            elif d==2:
                q.append((cx,cy,0))
            else:
                q.append((cx,cy,1))
    return sum(r)
print(bfs())