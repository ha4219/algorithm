from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)
for i in range(n):
    for j in range(n):
        if a[i][j]==9:
            start = (i,j)

def bfs():
    v = [[[[0]*10 for _ in range(10)] for __ in range(n)] for ___ in range(n)]
    q = deque()
    # x y size eat time
    res = 0
    q.append((start[0],start[1], 2, 0, 0))
    v[start[0]][start[1]][2][0] = 1
    while q:
        x,y,s,e,t = q.popleft()
        #res = max(res, t)
        for i in range(4):
            cx, cy = x+dx[i], y+dy[i]
            if cx<0 or cy<0 or cx>=n or cy>=n:
                continue
            if a[cx][cy]>s:
                continue
            elif 1<=a[cx][cy]<=s:
                if s<6 and e+1==s and not v[cx][cy][s+1][0]:
                    v[cx][cy][s+1][0] = 1
                    q.append((cx,cy,s+1,0,t+1))
                elif not v[cx][cy][s][min(e+1, 9)]:
                    v[cx][cy][s][min(e+1, 9)] = 1
                    q.append((cx,cy,s,min(e+1, 9),t+1))
                res = max(res, t+1)
            elif a[cx][cy]==0:
                if not v[cx][cy][s][e]:
                    v[cx][cy][s][e] = 1
                    q.append((cx,cy,s,e,t+1))
    return res
print(bfs())