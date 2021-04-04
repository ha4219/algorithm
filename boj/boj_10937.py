from sys import stdin


input = stdin.readline


n = int(input())
a0 = [input().strip() for _ in range(n)]
a = []
s = [[100,70,40,0],[70,50,30,0],[40,30,20,0],[0,0,0,0]]
d = [[-1]*(1<<(n+1)) for _ in range(n*n)]

for i in range(n):
    for j in range(n):
        if a0[i][j]=='A':
            a.append(0)
        elif a0[i][j]=='B':
            a.append(1)
        elif a0[i][j]=='C':
            a.append(2)
        else:
            a.append(3)

def dfs(x, path):
    if x==n*n:
        return 0
    if d[x][path]!=-1:
        return d[x][path]
    # 현 위치에 체크
    if path&1==1:
        d[x][path]=dfs(x+1,path>>1)
        return d[x][path]
    d[x][path]=0
    # right
    if x%n!=n-1 and path&2==0:
        d[x][path]=max(d[x][path],dfs(x+1,(path>>1)|1)+s[a[x]][a[x+1]])
    # down
    if x//n<n-1 and path&(1<<n)==0:
        d[x][path]=max(d[x][path],dfs(x+1,(path|(1<<n))>>1)+s[a[x]][a[x+n]])
    # none
    d[x][path]=max(d[x][path],dfs(x+1,path>>1))
    return d[x][path]

print(dfs(0,0))