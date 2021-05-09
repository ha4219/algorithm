from sys import stdin

input = stdin.readline

n,m=map(int,input().split())
a = list(map(int,input().split()))

def dfs(i, s, t):
    if t>=m or i>=n-1:
        return s
    res = dfs(i+1, s+a[i+1],t+1)
    if i+2<n:
        res = max(res,
         dfs(i+2, s//2+a[i+2], t+1))
    return res

print(dfs(-1,1,0))