from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

n,m,c=map(int,input().split())
a=list(map(int,input().split()))
d=[[[-1]*(1<<n) for _ in range(c+1)] for _ in range(m+1)]

all_path=(1<<n)-1

def dfs(b,cap,path):
    if path==all_path or b==m:
        return 0
    if d[b][cap][path]!=-1:
        return d[b][cap][path]
    d[b][cap][path] = 0
    for i in range(n):
        if (1<<i)&path or cap<a[i]:
            continue
        if cap-a[i]>0:
            d[b][cap][path]=max(d[b][cap][path],dfs(b,cap-a[i],path|(1<<i))+1)
        d[b][cap][path]=max(d[b][cap][path],dfs(b+1,c,path|(1<<i))+1)
    return d[b][cap][path]

print(dfs(0,c,0))