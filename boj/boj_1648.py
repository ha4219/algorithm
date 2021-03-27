from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline

n,m=map(int,input().split())
MOD = 9901
d =[[-1]*(1<<m) for _ in range(n*m)]

def dfs(c,path):
    if c==n*m and path==0:
        return 1
    if c>=n*m:
        return 0
    if d[c][path]!=-1:
        return d[c][path]
    d[c][path] = 0
    if path&1:
        d[c][path]=dfs(c+1,path>>1)
    else:
        d[c][path] = dfs(c+1,(path>>1)|(1<<(m-1)))
        if (c%m)!=(m-1) and (path&2)==0:
            d[c][path] += dfs(c+2, path>>2)
    return d[c][path] % MOD

print(dfs(0,0))