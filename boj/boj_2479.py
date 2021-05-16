from sys import stdin
from collections import deque

input = stdin.readline
n,k=map(int,input().split())

aa = [input().strip() for _ in range(n)]
start,end = map(int,input().split())
v = [0] * (n+1)
a = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            continue 
        t = 0
        for z in range(k):
            if aa[i][z]!=aa[j][z]:
                t += 1
        if t==1:
            a[i][j] = 1
            a[j][i] = 1

def bfs():
    q = deque()
    q.append((start-1,[start]))
    while q:
        x,res=q.popleft()
        if x == end-1:
            return res
        for i in range(n):
            if a[x][i] and v[i]==0:
                v[i] = 1
                q.append((i,res+[i+1]))
    return [-1]

print(*bfs())