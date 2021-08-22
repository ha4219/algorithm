from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int, input().split())

a = [input().strip() for _ in range(n)]

dx = (1,-1,0,0)
dy = (0,0,1,-1)

for i in range(n):
    for j in range(m):
        if a[i][j]=='C':
            start = (i,j)
        elif a[i][j]=='E':
            end = (i,j)

def dijktstra():
    pq = []
    heappush(pq, (0, start[0], start[1]))
    d = [[maxsize]*m for _ in range(n)]
    d[start[0]][start[1]] = 0
    while pq:
        health, x, y = heappop(pq)
        for i in range(4):
            cx, cy = x+dx[i], y+dy[i]
            flag = 0
            chealth = health
            if cx<0 or cy<0 or cx>=n or cy>=m:
                continue
            if a[cx][cy]=='X':
                cx, cy = cx+dx[0],cy+dy[0]
                while a[cx][cy]=='X' and cx>=0:
                    cx, cy = cx+dx[0],cy+dy[0]
                chealth += 10
                flag = 1
            if a[cx][cy]=='D':
                continue
            elif a[cx][cy]=='E' and d[cx][cy]>chealth:
                d[cx][cy] = chealth
                # heappush(pq, (chealth, cx, cy))
            elif (i==0 or i==1) and a[cx][cy]=='L' and d[cx][cy]>chealth+5:
                d[cx][cy] = chealth + 5
                heappush(pq, (d[cx][cy], cx, cy))
            elif flag and a[cx][cy]=='F' and d[cx][cy]>chealth:
                d[cx][cy] = chealth
                heappush(pq, (d[cx][cy], cx, cy))
            elif flag==0 and a[cx][cy]=='F' and d[cx][cy]>chealth+1:
                d[cx][cy] = chealth + 1
                heappush(pq, (d[cx][cy], cx, cy))
    return d[end[0]][end[1]]
print(dijktstra())