from sys import stdin, maxsize
from math import sqrt

input = stdin.readline

n = int(input())
a = [[0]*n for _ in range(n)]
xs=[]
ys=[]
for _ in range(n):
    x,y=map(int,input().split())
    xs.append(x)
    ys.append(y)
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        val = sqrt((xs[i]-xs[j])**2+(ys[i]-ys[j])**2)
        a[i][j] = val

d = [[0]*(1<<n) for _ in range(n)]

all_path = (1<<n) - 1


def tsp(cur, path):
    if path==all_path:
        return a[cur][0] if a[cur][0]>0 else maxsize
    if d[cur][path]:
        return d[cur][path]
    r = maxsize
    for i in range(1,n):
        if (path>>i)%2==1 or a[cur][i]==0:
            continue
        r = min(r, a[cur][i]+tsp(i,path|(1<<i)))
    d[cur][path] = r
    return r
print(tsp(0,1))