---
layout: post
title: boj 3056 해설
categories: [Baekjoon]
tags: [백준 1648, boj 1648]
---

백준 3056번
======

bitmasking, dp

-----
최근 bitmasking & dp 문제를 푸는데 비슷한 문제에 막혀서 한 가지 풀이를 보고 문제를 풀었다. 
 [boj 1648 참고 사이트](https://jaimemin.tistory.com/1123) 
nxm격자가 있을 때 격자에 2x1, 1x2격자를 채우는 문제이다. 풀이는 첫번째 칸부터 m개의 격칸들을 비트마스킹으로 확인하는 것이다. 
1. if path&1:
현재 위치한 칸이 채워져있으면 다음 칸을 확인한다. dfs(current+1, path>>1)
이때 path>>1은 다음 칸 위치에서는 현재 칸 값이 필요없기에 shift연산을 해준다.
2-1. 현재 칸에 2*1 격자를 배치한다. 
따라서 dfs(current+1,path>>1(1<<(m-1))) 현재 칸에서는 m만큼 차이가 나지만 다음 칸에서 m-1만큼 차이나기에 path값을 위와 같이 준다.
2-2. 1*2 격자를 두는 경우이다. 먼저 우측에 격자를 둘수 있는지 확인하고 다음칸에도 격자가 없으면 dfs(current+2,path>>2)를 통해 2칸 뒤 값을 확인한다.

마지막으로 기저부분에서 모든 칸이 채워질 경우 1을 반환한다...

```python
from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline

n,m=map(int,input().split())
MOD = 9901
d =[[-1]*(1<<m) for _ in range(n*m)]

def dfs(c,path):
    if c==n*m and path==0:
        return 1
    if c>=n*m:
        return 0
    if d[c][path]!=-1:
        return d[c][path]
    d[c][path] = 0
    if path&1:
        d[c][path]=dfs(c+1,path>>1)
    else:
        d[c][path] = dfs(c+1,(path>>1)|(1<<(m-1)))
        if (c%m)!=(m-1) and (path&2)==0:
            d[c][path] += dfs(c+2, path>>2)
    return d[c][path] % MOD

print(dfs(0,0))
```