from sys import stdin
from heapq import *

input = stdin.readline

n = int(input())
m = int(input())
a = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    p,q,r=map(int,input().split())
    
    if q==1:
        a[p-1][n] = r
    else:
        a[p-1][q-1] = r
    

# d = [[0]*(n+1) for _ in range(n+1)]
p = [-1] * (n+1)
def dijkstra(start, end):
    pq = [(0, start)]
    d = [0] * (n+1)
    while pq:
        cost, x = heappop(pq)
        cost = -cost
        # print(cost, x+1)
        for i in range(n+1):
            if a[x][i]!=0 and cost+a[x][i]>d[i]:
                p[i] = x
                d[i]=cost+a[x][i]
                heappush(pq,(-d[i],i))
    return d[i]

print(dijkstra(0,n))
res = []
c = n
while c!=-1:
    if c==n:
        res.append(1)
    else:
        res.append(c+1)
    c = p[c]
print(*res[::-1])

