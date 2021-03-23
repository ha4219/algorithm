2021-03-23-boj 17182.md


---
layout: post
title: boj 17182 해설
categories: [Baekjoon]
tags: [백준 17182, boj 17182]
---

# 백준 17182번

## Floyd Warshall, Bitmasking

문제 핵심은 **"탐사 후 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다."** 이다. 처음 문제를 풀었을 때 이 문장을 안읽어 답이 틀렸었는데 다시 읽어보니 쉽게 이해할 수 있었다. 2<=**n**<=10으로 매우 작다. 따라서 n^3인 floyd warshall 가능!

```python
from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

n, k = map(int, input().split())
aa = [list(map(int, input().split())) for _ in range(n)]
d = [[maxsize]*(1<<n) for _ in range(n)]

a = [[maxsize]*n for _ in range(n)]

all_path = (1<<n) - 1

for i in range(n):
    for j in range(n):
        for p in range(n):
            a[i][j]=min(a[i][j],aa[i][p]+aa[p][j])

def dfs(cur, path):
    if path==all_path:
        return 0
    for i in range(n):
        if path & (1<<i):
            continue
        d[cur][path] = min(d[cur][path],dfs(i, path|(1<<i))+a[cur][i])
    return d[cur][path]
print(dfs(k, (1<<k)))
```