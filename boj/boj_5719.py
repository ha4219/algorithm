from sys import stdin, maxsize
from heapq import *


input = stdin.readline

def dijkstra(s,d):
    v[s] = 0
    pq = [[0,s]]
    while pq:
        cost, x = heappop(pq)
        for i in range(n):
            if dist[x][i]>0 and v[i]>dist[x][i]+cost:
                v[i] = dist[x][i]+cost
                p[i] = x
                heappush(pq, [dist[x][i]+cost, i])
    return -1 if v[d]==maxsize else v[d]

def r(s,d):
    pq = [[v[d], d]]
    while pq:
        cost,x=heappop(pq)
        for i in range(n):
            if dist[i][x]>0 and v[i]==(cost-dist[i][x]):
                dist[i][x] = -1
                heappush(pq, [v[i], i])
    return 

while 1:
    n,m=map(int,input().split())
    if n==m and m==0:
        break
    dist = [[-1] * n for _ in range(n)]
    p = [-1] * n 
    s,d=map(int,input().split())
    for _ in range(m):
        z,x,c=map(int,input().split())
        dist[z][x] = c
    v = [maxsize] * n
    t = dijkstra(s,d)
    if t==-1:
        print(-1)
    else:
        r(s,d)
        v = [maxsize] * n
        print(dijkstra(s,d))