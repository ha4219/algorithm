from sys import stdin


input = stdin.readline


n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[-1]*(1<<n) for _ in range(n)]
p = [0] * n

for i in range(n):
    for j in range(i+1,n):
        if a[j][0]%a[i][0]==0:
            p[j] |= (1<<i)

# for i in range(n):
#     print(i,(bin(p[i])[2:]).zfill(n))

def dfs(r,path):
    if r==n:
        return 0
    if d[r][path]!=-1:
        return d[r][path]
    d[r][path] = 0
    for i in range(n):
        if ((path&(1<<i))==0) and ((p[i]&path) == p[i]):
            d[r][path] = max(d[r][path],dfs(r+1,path|(1<<i))+a[i][1]*(r+1))
    return d[r][path]

print(dfs(0,0))