from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx, dy = (1,-1,0,0), (0,0,1,-1)

def bfs():
    q = deque()
    v = [[[[0]*4 for _ in range(101)]\
         for __ in range(n)] for ____ in range(n)]
    v[0][0][1] = [1,1,1,1]
    if a[1][0]!=1:
        q.append((1,0,1,0,1))
        v[1][0][1][0] = 1
    if a[0][1]!=1:
        q.append((0,1,1,2,1))
        v[0][1][1][2] = 1
    # x y speed direction
    # v = [[0] * n for _ in range(n)]
    
    while q:
        x,y,sp,d,t = q.popleft()
        # print(x,y,sp,d,t)
        if x==n-1 and y==n-1:
            return t
        for i in range(4):
            if i==d:
                speed = sp+1
                cx,cy = x+dx[i]*speed,y+dy[i]*speed
            else:
                speed = 1
                cx,cy = x+dx[i]*speed, y+dy[i]*speed
            if cx<0 or cy<0 or cx>=n or cy>=n\
                 or v[cx][cy][speed][i] or (a[cx][cy] and a[cx][cy]<=t+1):
                continue
            tmp = 0
            for j in range(1, speed):
                if a[x+dx[i]*j][y+dy[i]*j]!=0 and a[x+dx[i]*j][y+dy[i]*j]<=t:
                    tmp = 1
                    break
            if tmp:
                continue
            v[cx][cy][speed][i] = 1
            q.append((cx,cy,speed,i,t+1))
    return -1
res = bfs()
print('Fired' if res==-1 else res)