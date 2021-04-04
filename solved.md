---
layout: post
title: boj 21321 해설
categories: [Baekjoon]
tags: [백준 21321, boj 21321]
---

백준 21321번
======

dp, bitmasking

-----
dp, 비트 마스킹 문제이다. 이전에 풀었던 문제와 다른 점은 특정 시간에 겹칠 경우 경로가 짧은 경로 순으로 점수를 획득할 수 있다. 따라서 이에 대한 연산이 따로 필요하다.

나는 p라는 배열에 각 경로 별 필요한 경로를 담았다. 
```python
for i in range(n):
    for j in range(i+1,n):
        if a[j][0]%a[i][0]==0:
            p[j] |= (1<<i)
```
i번째 경로와 j번째 경로가 겹칠 경우 p[j]에 i번째 비트를 켰다. 

```python
if ((path&(1<<i))==0) and ((p[i]&path) == p[i]):
    // DO
```
저장한 p값은 탐색 중 가지고 있는 path와 비교해 현재 경로를 접근할 수 있는지 확인할 수 있게 했다.

마지막으로 필요한 경로를 설정하는 시간복잡도 O(n^2)이다.
n이 16이하 자연수이기에 해결 가능하다.

```python
from sys import stdin


input = stdin.readline


n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[-1]*(1<<n) for _ in range(n)]
p = [0] * n

for i in range(n):
    for j in range(i+1,n):
        if a[j][0]%a[i][0]==0:
            p[j] |= (1<<i)

# for i in range(n):
#     print(i,(bin(p[i])[2:]).zfill(n))

def dfs(r,path):
    if r==n:
        return 0
    if d[r][path]!=-1:
        return d[r][path]
    d[r][path] = 0
    for i in range(n):
        if ((path&(1<<i))==0) and ((p[i]&path) == p[i]):
            d[r][path] = max(d[r][path],dfs(r+1,path|(1<<i))+a[i][1]*(r+1))
    return d[r][path]

print(dfs(0,0))
```