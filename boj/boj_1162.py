from sys import stdin,maxsize
from heapq import *


input = stdin.readline

def dijkstra(start):
    pq = [[0,start,0]]
    v = [[maxsize] * (21) for _ in range(n+1)]
    v[start][0] = 0
    while pq:
        tt, xx, kk = heappop(pq)
        if tt > v[xx][kk]:
            continue
        for next, ttt in a[xx]:
            if kk+1<=k:
                if v[next][kk+1]>v[xx][kk]:
                    v[next][kk+1]=v[xx][kk]
                    heappush(pq, [v[next][kk+1], next, kk+1])
                if v[next][kk]>v[xx][kk]+ttt:
                    v[next][kk]=v[xx][kk]+ttt
                    heappush(pq, [v[next][kk], next, kk])
            else:
                if v[next][kk]>v[xx][kk]+ttt:
                    v[next][kk]=v[xx][kk]+ttt
                    heappush(pq, [v[next][kk], next, kk])
    return min(v[n])


n,m,k=map(int,input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,d=map(int,input().split())
    a[u].append((v,d))
    a[v].append((u,d))
print(dijkstra(1))