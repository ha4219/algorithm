from sys import stdin,maxsize
from heapq import *


input = stdin.readline

def dijkstra(start):
    v = [maxsize] * (n+1)
    pq = [[0,start]]
    v[c] = 0
    rec = 0
    res = 0
    while pq:
        tt, xx = heappop(pq)
        for next, ttt in a[xx]:
            if v[next]<=v[xx]+ttt:
                continue
            v[next] = v[xx]+ttt
            heappush(pq, [tt+ttt,next])
    for i in range(1,n+1):
        if v[i]!=maxsize:
            rec += 1
            res = max(res,v[i])
    return [rec,res]

for _ in range(int(input())):
    n,d,c=map(int,input().split())
    a = [[] for _ in range(n+1)]
    for _ in range(d):
        p,q,t=map(int,input().split())
        a[q].append((p,t))


    print(*dijkstra(c))