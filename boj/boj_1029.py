from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


n = int(input())
aa = [input().strip() for _ in range(n)]
a = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i].append(int(aa[i][j]))
d = [[[-1]*(1<<15) for __ in range(10)]for _ in range(n+1)]


def dfs(f,p,path):
    if d[f][p][path]!=-1:
        return d[f][p][path]
    d[f][p][path]=1
    for i in range(n):
        if (1<<i)&path:
            continue
        if a[f][i]>=p:
            d[f][p][path]=max(d[f][p][path],1+dfs(i,a[f][i],path|(1<<i)))
    return d[f][p][path]
print(dfs(0,0,1))        