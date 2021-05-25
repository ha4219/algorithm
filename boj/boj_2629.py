from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

n = int(input())
a = list(map(int,input().split())) + [0]
MAX = 15001
d = [[0] * MAX for _ in range(n+1)]

def dfs(i, w):
    if i>n:
        return 
    if d[i][w]:
        return
    d[i][w] = 1
    dfs(i+1,w)
    dfs(i+1,w+a[i])
    dfs(i+1,abs(w-a[i]))

dfs(0,0)
m = int(input())
r = list(map(int,input().split()))

res = []
for i in range(m):
    if r[i]>=MAX:
        res.append('N')
    else:
        res.append('Y' if d[n][r[i]] else 'N')
print(*res)