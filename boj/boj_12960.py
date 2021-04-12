from sys import stdin


input = stdin.readline

n, m = map(int,input().split())
aa=[input().strip() for _ in range(n)]
a = ''

for i in range(m):
    for j in range(n):
        a += aa[j][i]

d = [[-1] * (1<<(n+3)) for _ in range(n*m)]

def dfs(x, path):
    if x>=n*m:
        return 0
    if d[x][path]!=-1:
        return d[x][path]
    if a[x]=='X' or path&1:
        d[x][path] = max(d[x][path],
            dfs(x+1,path>>1))
        return d[x][path]
    # print(x)
    if x%n!=n-1 and x//n!=m-1:
        # 00
        # 0
        t = 1 | 2 | (1<<n)
        if a[x]=='.' and a[x+1]=='.' and a[x+n]=='.' and path&t==0:
            d[x][path] = max(d[x][path], dfs(x+1,(path>>1)|(t>>1))+1)
        # 00
        #  0
        t = 1 | (1<<n) | (1<<(n+1))
        if a[x]=='.' and a[x+n]=='.' and a[x+n+1]=='.' and path&t==0:
            d[x][path] = max(d[x][path], dfs(x+1,(path>>1)|(t>>1))+1)
        #  0
        # 00
        t = 2 | (1<<n) | (1<<(n+1))
        if a[x+n+1]=='.' and a[x+1]=='.' and a[x+n]=='.' and path&t==0:
            d[x][path] = max(d[x][path], dfs(x+1,(path>>1)|(t>>1))+1)
        # 0
        # 00
        t = 1 | 2 | (1<<(n+1))
        if a[x]=='.' and a[x+1]=='.' and a[x+n+1]=='.' and path&t==0:
            d[x][path] = max(d[x][path], dfs(x+1,(path>>1)|(t>>1))+1)
    d[x][path] = max(d[x][path],
        dfs(x+1,path>>1))
    return d[x][path]
print(dfs(0,0))
