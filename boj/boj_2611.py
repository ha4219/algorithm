from sys import stdin, setrecursionlimit
from heapq import *

input = stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
for _ in range(m):
    p,q,r=map(int,input().split())
    if q==1:
        a[p-1].append((n, r))
        # a[p-1][n] = r
    else:
        # a[p-1][q-1] = r
        a[p-1].append((q-1, r))
    

# d = [[0]*(n+1) for _ in range(n+1)]
p = [-1] * (n+1)

def dijkstra(start, end):
    pq = [(0, start)]
    d = [0] * (n+1)
    while pq:
        cost, x = heappop(pq)
        cost = -cost
        # print(cost, x+1)
        # for i in range(n+1):
        #     if a[x][i]!=0 and cost+a[x][i]>d[i]:
        #         p[i] = x
        #         d[i]=cost+a[x][i]
        #         heappush(pq,(-d[i],i))
        for i,c in a[x]:
            if cost+c>d[i]:
                p[i] = x
                d[i] = cost + c
                heappush(pq, (-d[i], i))
    return d[n]
# d = [-1] * (n+1)
# def dfs(idx, cost):
#     # print(a[idx])
#     for i,c in a[idx]:
#         if d[i] < cost+c:
#             d[i] = cost+c
#             dfs(i, cost+c)
#             p[i] = idx
#     # return d[idx]
# dfs(0,0)
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

