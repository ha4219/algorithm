from sys import stdin

input = stdin.readline

n, m = map(int,input().split())
a = [input().strip() for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)



for i in range(n):
    for j in range(m):
        if a[i][j]=='I':
            start = (i,j)

def bfs():
    from collections import deque


    v = [[0]*m for _ in range(n)]
    q = deque()
    q.append((start[0],start[1]))
    res = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            cx,cy=x+dx[i],y+dy[i]
            if cx<0 or cy<0 or cx>=n or cy>=m or v[cx][cy] or a[cx][cy]=='X':
                continue
            if a[cx][cy]=='P':
                res += 1
            v[cx][cy] = 1
            q.append((cx,cy))
    return res
ret = bfs()
print('TT' if ret==0 else ret)