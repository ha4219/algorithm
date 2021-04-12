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
    if a[x]=='1' or path&1:
        d[x][path] = max(d[x][path],
            dfs(x+1,path>>1)+1)
        return d[x][path]
    if x%n!=n-1 and x//n!=m-1 and (path&1)==0 and (path&2)==0 and (path&(1<<n))==0 and (path&(1<<(n+1)))==0 and a[x]!='1' and a[x+1]!='1' and a[x+n]!='1' and a[x+n+1]!='1':
        t = (path>>1)
        t|=(1<<0)
        t|=(1<<(n-1))
        t|=(1<<n)
        d[x][path]=max(d[x][path],dfs(x+1,t)+13)
    d[x][path] = max(d[x][path],
        dfs(x+1,path>>1)+1)
    return d[x][path]
print(dfs(0,0))