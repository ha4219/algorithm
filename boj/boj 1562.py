from sys import stdin


input = stdin.readline

n = int(input())
d = [[[-1] * (1<<10) for _ in range(11)] for __ in range(n+1)]
t = [(1<<i) for i in range(10)]
mod = 10**9
for i in range(1,10):
    d[1][i][(1<<i)]=1

def dfs(p,s,path):
    if s<0 or s>9:
        return 0
    if p==1:
        if (path|(1<<s))==((1<<10)-1):
            return 1
        else:
            return 0
    if d[p][s][path]!=-1:
        return d[p][s][path]
    path |= t[s]
    d[p][s][path]=(dfs(p-1,s+1,path)+dfs(p-1,s-1,path))%mod
    return d[p][s][path]
res = 0
for i in range(1,10):
    res = (res+dfs(n,i,0))%mod
print(res)