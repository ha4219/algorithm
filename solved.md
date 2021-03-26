---
layout: post
title: boj 3056 해설
categories: [Baekjoon]
tags: [백준 3056, boj 3056]
---

백준 3056번
======

bitmasking, dp

cur은 현재 매칭할 요원 index이고 path는 매칭된 요원들을 나타낸다. 여기 문제 핵심은 모든 방문을 끝내면 1을 반환한다. 왜냐하면 확률을 계산하는게 곱연산이기에 dfs()*a 연산에 영향을 안주기 위해 1을 반환한다. 
-----

```python
from sys import stdin


input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * (1<<n) for _ in range(n)]

all_path = (1<<n)-1
def dfs(cur, path):
    if path==all_path:
        return 1
    if d[cur][path]!=-1:
        return d[cur][path]
    d[cur][path] = 0
    for i in range(n):
        if path&(1<<i):
            continue
        d[cur][path] = max(d[cur][path], dfs(cur+1,path|(1<<i))*(a[cur][i])/100)
    return d[cur][path]

print(dfs(0,0)*100)
```