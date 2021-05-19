from sys import stdin

input = stdin.readline

n,m=map(int,input().split())
hx,hy=map(int,input().split())
ex,ey=map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)


def bfs():
    v = [[[0]*2 for _ in range(m)] for __ in range(n)]
    q = deque()
    if a[hx-1][hy-1]==1:
        q.append((hx-1,hy-1,1))
        v[hx-1][hy-1][1] = 1
    else:
        q.append((hx-1,hy-1,0))
        v[hx-1][hy-1][0] = 1
    d = -1
    while q:
        d += 1
        for _ in range(len(q)):
            x,y,c=q.popleft()
            if x==ex-1 and y==ey-1:
                return d
            for i in range(4):
                cx,cy=x+dx[i],y+dy[i]
                if cx<0 or cy<0 or cx>=n or cy>=m:
                    continue
                if a[cx][cy]:
                    if c==0 and v[cx][cy][1]==0:
                        v[cx][cy][1]=1
                        q.append((cx,cy,1))
                else:
                    if v[cx][cy][c]==0:
                        v[cx][cy][c] = 1
                        q.append((cx,cy,c))
    return -1

print(bfs())