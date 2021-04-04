---
layout: post
title: boj 1657 해설
categories: [Baekjoon]
tags: [백준 1657, boj 1657]
---

[백준 1657번](https://www.acmicpc.net/problem/1657)
======

dp, bitmasking

-----
[백준 10937번](https://www.acmicpc.net/problem/10937)

똑같은 문제다...


```python
from sys import stdin


input = stdin.readline


n,m = map(int,input().split())
a0 = [input().strip() for _ in range(n)]
a = []
s = [[10,8,7,5,1],[8,6,4,3,1],[7,4,3,2,1],[5,3,2,2,1],[1,1,1,1,0]]
d = [[-1]*(1<<(m+1)) for _ in range(n*m)]

for i in range(n):
    for j in range(m):
        if a0[i][j]=='A':
            a.append(0)
        elif a0[i][j]=='B':
            a.append(1)
        elif a0[i][j]=='C':
            a.append(2)
        elif a0[i][j]=='D':
            a.append(3)
        else:
            a.append(4)

def dfs(x, path):
    if x==n*m:
        return 0
    if d[x][path]!=-1:
        return d[x][path]
    # 현 위치에 체크
    if path&1==1:
        d[x][path]=dfs(x+1,path>>1)
        return d[x][path]
    d[x][path]=0
    # right
    if x%m!=m-1 and path&2==0:
        d[x][path]=max(d[x][path],dfs(x+1,(path>>1)|1)+s[a[x]][a[x+1]])
    # down
    if x//m<n-1 and path&(1<<m)==0:
        d[x][path]=max(d[x][path],dfs(x+1,(path|(1<<m))>>1)+s[a[x]][a[x+m]])
    # none
    d[x][path]=max(d[x][path],dfs(x+1,path>>1))
    return d[x][path]

print(dfs(0,0))
```