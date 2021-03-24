---
layout: post
title: boj 1480 해설
categories: [Baekjoon]
tags: [백준 1480, boj 1480]
---

백준 1480번
======

dp, Bitmasking
-----

호호호!
```
세준이는 잘 모르겠지만, 세준이는 보석에 미쳐있다.
따라서, 숌 보석상에 있는 모든 보석을 다훔치려고 한다.
하지만, 세준이는 보석을 다 가져올 수는 없다. 그 이유는 가방의 개수에 제한이 있고,
한 가방마다 넣을 수 있는 보석의 개수가 제한이 있기 때문이다. 세준이는 M개의 가방을 가지고 있다.
그리고 각각의 가방은 C그램의 보석을 담을 수 있다.
```
위 설명처럼 핵심은 아래와 같다. 
*현 위치에서 보석을 담을 경우
    *이럴 경우 dfs(bag,cap-a[i],path|(1<<i))로 현재 가방에서 용량을 a[i]만큼 용량을 줄이고 다음을 탐색하는 경우이다.
*현 위치에서 보석을 안담고 다음 가방 탐색
    *이럴 경우는 dfs(bag+1,c,path|(1<<i))로 다음 가방에 담는 것이다.

```python
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

n,m,c=map(int,input().split())
a=list(map(int,input().split()))
d=[[[-1]*(1<<n) for _ in range(c+1)] for _ in range(m+1)]

all_path=(1<<n)-1

def dfs(b,cap,path):
    if path==all_path or b==m:
        return 0
    if d[b][cap][path]!=-1:
        return d[b][cap][path]
    d[b][cap][path] = 0
    for i in range(n):
        if (1<<i)&path or cap<a[i]:
            continue
        if cap-a[i]>0:
            d[b][cap][path]=max(d[b][cap][path],dfs(b,cap-a[i],path|(1<<i))+1)
        d[b][cap][path]=max(d[b][cap][path],dfs(b+1,c,path|(1<<i))+1)
    return d[b][cap][path]

print(dfs(0,c,0))
```