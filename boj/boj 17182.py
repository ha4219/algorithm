from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

n, k = map(int, input().split())
aa = [list(map(int, input().split())) for _ in range(n)]
d = [[maxsize]*(1<<n) for _ in range(n)]

a = [[maxsize]*n for _ in range(n)]

all_path = (1<<n) - 1

for i in range(n):
    for j in range(n):
        for p in range(n):
            a[i][j]=min(a[i][j],aa[i][p]+aa[p][j])

def dfs(cur, path):
    if path==all_path:
        return 0
    for i in range(n):
        if path & (1<<i):
            continue
        d[cur][path] = min(d[cur][path],dfs(i, path|(1<<i))+a[cur][i])
    return d[cur][path]
print(dfs(k, (1<<k)))