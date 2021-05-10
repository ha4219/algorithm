from sys import stdin, maxsize
from collections import deque

input = stdin.readline


n, m =map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]
dx = (1,0)
dy = (0,1)

v = [[maxsize]*m for _ in range(n)]

def bfs():
    q = deque()
    v[0][0] = 1
    q.append((0,0,0))
    while q:
        x,y,c=q.popleft()
        for i in range(1,a[x][y]+1):
            for j in range(2):
                cx,cy = x+dx[j]*i,y+dy[j]*i
                if cx<0 or cy<0 or cx>=n or cy>=m or v[cx][cy]<=c+1:
                    continue
                v[cx][cy] = min(v[cx][cy],c+1)
                q.append((cx,cy,c+1))
    return v[n-1][m-1]
print(bfs())