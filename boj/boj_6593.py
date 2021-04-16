from sys import stdin
from collections import deque

input = stdin.readline



dz = (1,-1,0,0,0,0)
dx = (0,0,1,-1,0,0)
dy = (0,0,0,0,1,-1)

def bfs(z,n,m):
    a = [[] for __ in range(z)]
    for k in range(z):
        if k>0:
            input()
        a[k] = [input().strip() for _ in range(n)]
        
    for k in range(z):
        for i in range(n):
            for j in range(m):
                if a[k][i][j]=='S':
                    start = (k,i,j)
                elif a[k][i][j]=='E':
                    end = (k,i,j)
    
    v = [[[0]*m for _ in range(n)] for __ in range(z)]
    q = deque()
    q.append((start[0],start[1],start[2], 0))
    v[start[0]][start[1]][start[2]] = 1
    while q:
        zz,x,y,t = q.popleft()
        # print(zz,x,y,t)
        if zz==end[0] and x==end[1] and y==end[2]:
            return t
        for i in range(6):
            cz,cx,cy=zz+dz[i],x+dx[i],y+dy[i]
            if cz<0 or cz>=z or cx<0 or cx>=n or cy<0 or cy>=m or v[cz][cx][cy] or a[cz][cx][cy]=='#':
                continue
            v[cz][cx][cy] = 1
            q.append((cz,cx,cy, t+1))
    return -1
while 1:
    z,n,m=map(int,input().split())
    if z==0 and n==0 and m==0:
        break
    res = bfs(z,n,m)
    print("Trapped!" if res==-1 else 'Escaped in %d minute(s).'%res)
    input()