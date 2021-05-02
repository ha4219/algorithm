from sys import stdin, setrecursionlimit
from collections import deque


dx = (1,-1,0,0)
dy = (0,0,1,-1)

n, m = map(int,input().split())
n, m = m, n
a = [list(map(int,input().split())) for _ in range(n)]

q = deque()
zero = 0
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            zero+=1
        elif a[i][j]==1:
            q.append((i,j))

def bfs(zero):
    ze = zero
    d = 0
    if ze==0:
        return d
    v = [[0]*m for _ in range(n)]
    while q:
        ql = len(q)
        d += 1
        for _ in range(ql):
            x,y = q.popleft()
            print(x,y)
            if ze==0:
                return d
            for i in range(4):
                cx,cy=x+dx[i],y+dy[i]
                if cx<0 or cx>=n or cy<0 or cy>=m or v[cx][cy] or a[cx][cy]!=0:
                    continue
                v[cx][cy] = 1
                ze -= 1
                if ze==0:
                    return d
                q.append((cx,cy))
    return -1
print(bfs(zero))