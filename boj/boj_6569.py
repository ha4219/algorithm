from sys import stdin


input = stdin.readline

def dfs(x, path):
    if x==n*m:
        return 1
    # print(x,path)
    if d[x][path]!=-1:
        return d[x][path]
    d[x][path] = 0
    # 현위치
    if path&1:
        # print('ch',x,path)
        d[x][path]+=dfs(x+1,path>>1)
        return d[x][path]
    # 현위치 b X, 우측에 b 설치
    if x%m!=m-1 and path&2==0:
        # print('r',x,path)
        d[x][path]+=dfs(x+1,(path>>1)|1)
    if x//m<n-1:
        # print('d',x,path)
        d[x][path]+=dfs(x+1,(path>>1)|(1<<(m-1)))
    return d[x][path]

n,m=map(int,input().split())
while n!=0 and m!=0:
    d = [[-1]*(1<<(m+2)) for _ in range(n*m)]
    print(dfs(0,0))
    n,m=map(int,input().split())