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
    d[i][k] = pe[i-1] if k else 0
    for j in a[i]:
        if v[j]:
            continue
        v[j] = 1
        if k:
            d[i][k] += dfs(j,0)
        else:
            d[i][k] += max(dfs(j,0),dfs(j,1))
        v[j] = 0
    return d[i][k]
res = []

def rdfs(i,k):
    if k==1:
        res.append(i)
    for j in a[i]:
        if v[j]:
            continue
        v[j] = 1
        if k==0:
            rdfs(j,1 if d[j][1]>d[j][0] else 0)
        else:
            rdfs(j,0)
        v[j] = 0

v[1] = 1
print(max(dfs(1,0),dfs(1,1)))
rdfs(1,d[1][1]>d[1][0])
res.sort()
print(*res)