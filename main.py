from sys import stdin


input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * (1<<n) for _ in range(n)]

all_path = (1<<n)-1
def dfs(cur, path):
    if path==all_path:
        return 1
    if d[cur][path]!=-1:
        return d[cur][path]
    d[cur][path] = 0
    for i in range(n):
        if path&(1<<i):
            continue
        d[cur][path] = max(d[cur][path], dfs(cur+1,path|(1<<i))*(a[cur][i]/100))
    return d[cur][path]

print(dfs(0,0)*100)