from sys import stdin


input = stdin.readline

# 틀림...
def dfs(cnt,money,path):
    if cnt==c:
        return 1
    if d[cnt][path]!=-1:
        return d[cnt][path]
    for i in range(n):
        if path&(1<<i) or money-a[i][0]<0:
            continue
        d[cnt][path]=max(d[cnt][path], dfs(cnt+1,money-a[i][0],path|(1<<i))*(a[i][1])/100)
    return d[cnt][path]

for __ in range(int(input())):
    n, c, m = map(int,input().split())

    d = [[-1]*(1<<n) for _ in range(c)]
    a = [list(map(int,input().split())) for _ in range(n)]


    print(dfs(0,m,0))