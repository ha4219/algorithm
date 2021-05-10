from sys import stdin, maxsize, setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline

n,s,m=map(int,input().split())
a = list(map(int,input().split()))
d = [[-2]*(m+1) for _ in range(n+1)]


def dfs(i,v):
    if i==n:
        return v;
    if d[i][v]!=-2:
        return d[i][v]
    d[i][v] = -1
    if 0<=v+a[i]<=m:
        d[i][v] = max(d[i][v], dfs(i+1,v+a[i]))
    if 0<=v-a[i]<=m:
        d[i][v] = max(d[i][v], dfs(i+1,v-a[i]))
    return d[i][v]

print(dfs(0,s))