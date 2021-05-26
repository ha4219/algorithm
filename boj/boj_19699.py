from sys import stdin, setrecursionlimit
from math import *

setrecursionlimit(10**6)

input = stdin.readline

MAX = 10001
p = [1] * MAX
p[0] = 0
p[1] = 0

for i in range(2, int(sqrt(MAX))+2):
    if p[i]==0:
        continue
    for j in range(i*2,MAX,i):
        if j>MAX:
            break
        p[j] = 0

n, m =map(int,input().split())
a = list(map(int,input().split()))+[0]
d = [[-1]*MAX for _ in range(n+1)]

def dfs(i,c,w):
    if c>m or i>n:
        return
    if d[i][w]!=-1:
        return
    if c==m:
        d[i][w] = 1

    dfs(i+1,c,w)
    dfs(i+1,c+1,w+a[i])
dfs(0,0,0)
res = []
for i in range(MAX):
    if d[n][i]==1 and p[i]:
        res.append(i)
if res:
    print(*res)
else:
    print(-1)