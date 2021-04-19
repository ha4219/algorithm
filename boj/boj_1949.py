from sys import stdin,setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

n=int(input())
pe=list(map(int,input().split()))
a=[[] for _ in range(n+1)]
v=[0]*(n+1)
d=[[-1]*2 for _ in range(n+1)]
for _ in range(n-1):
    p,q=map(int,input().split())
    a[p].append(q)
    a[q].append(p)

def dfs(i,k):
    if d[i][k]!=-1:
        return d[i][k]
    v[i]=1
    r = pe[i-1] if k!=1 else 0
    for j in a[i]:
        if v[j]:
            continue
        t = dfs(j,1)
        if k==1:
            t = max(t,dfs(j,0))
        r+=t
    v[i]=0
    d[i][k] = r
    return d[i][k]
print(max(dfs(1,0),dfs(1,1)))