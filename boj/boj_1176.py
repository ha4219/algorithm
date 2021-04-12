from sys import stdin


input = stdin.readline


n,k=map(int,input().split())
a = [int(input()) for _ in range(n)]
d = [[[-1]*(1<<n) for __ in range(n)] for _ in range(n)]

def dfs(f, idx, tall, path):
    if f==n:
        return 1
    if d[f][idx][path]!=-1:
        return d[f][idx][path]
    d[f][idx][path] = 0
    for i in range(n):
        if f==0:
            d[f][idx][path] += dfs(f+1,i,a[i],path|(1<<i))
        else:
            if path&(1<<i):
                continue
            if abs(tall-a[i])>k:
                d[f][idx][path] += dfs(f+1,i, a[i], path|(1<<i))
    return d[f][idx][path]

print(dfs(0,0,0,0))