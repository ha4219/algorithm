---
layout: post
title: boj 1562 해설
categories: [Baekjoon]
tags: [백준 1562, boj 1562]
---

# 백준 1562번

## dp, Bitmasking

처음에는 이중 for문으로 가능할까 생각했지만 path, 0~9까지 숫자가 모두 사용해야 함으로 dfs 함수를 사용했다. 모든 수를 거쳤을 때, path==(1<<10)-1이여야 return 1을 반납하여 개수를 측정했다.

```python
from sys import stdin


input = stdin.readline

n = int(input())
d = [[[-1] * (1<<10) for _ in range(11)] for __ in range(n+1)]
mod = 10**9
for i in range(1,10):
    d[1][i][(1<<i)]=1

def dfs(p,s,path):
    if s<0 or s>9:
        return 0
    if p==1:
        if (path|(1<<s))==((1<<10)-1):
            return 1
        else:
            return 0
    if d[p][s][path]!=-1:
        return d[p][s][path]
    path |= t[s]
    d[p][s][path]=(dfs(p-1,s+1,path)+dfs(p-1,s-1,path))%mod
    return d[p][s][path]
res = 0
for i in range(1,10):
    res = (res+dfs(n,i,0))%mod
print(res)
```