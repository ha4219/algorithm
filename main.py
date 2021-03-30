from sys import stdin, maxsize
from collections import deque

input=stdin.readline


n = int(input())
a = [[0,0]]+[list(map(int,input().split())) for _ in range(n-1)]
k = int(input())

q=deque()
q.append((1,0,0))
def bfs():
    res = maxsize
    v = [maxsize] * (n+1)
    while q:
        x,e,c=q.popleft()
        if x==n:
            res = min(e,res)
            continue
        if x<1 or x>n:
            continue
        if e>v[x]:
            continue
        v[x] = e
        q.append((x+1,e+a[x][0],c))
        q.append((x+2,e+a[x][1],c))
        # q.append((x-1,e+a[x][0],c))
        # q.append((x-2,e+a[x][1],c))
        if c==0:
            q.append((x+3,e+k,1))
            # q.append((x-3,e+k,1))
    return res
print(bfs())
        
# d = [[-1] * (n+1) for _ in range(2)]

# def dfs(x,e,c):
#     if x==n:
#         return e
#     if x<1 or x>n:
#         return maxsize
#     if d[c][x]!=-1:
#         return d[c][x]
#     d[c][x] = maxsize
#     d[c][x] = min(d[c][x], dfs(x+1,e+a[x][0],c))
#     d[c][x] = min(d[c][x], dfs(x+2,e+a[x][1],c))
#     d[c][x] = min(d[c][x], dfs(x-1,e+a[x][0],c))
#     d[c][x] = min(d[c][x], dfs(x-2,e+a[x][1],c))

#     if c==0:
#         d[c][x] = min(d[c][x], dfs(x+3,e+k,1))
#         d[c][x] = min(d[c][x], dfs(x-3,e+k,1))
#     return d[c][x]
# print(dfs(1,0,0))