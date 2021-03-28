---
layout: post
title: boj 21312 해설
categories: [Baekjoon]
tags: [백준 21312, boj 21312]
---

백준 21312번
======

combinations, brute force

-----
n이 3인 arr에서 부분 집합의 곱을 도출하는데 홀수 값이 있을 경우 최대값을 출력하고 홀수 값이 없을 경우 짝수 중 최대값을 출력한다. 

매우쉬움...

```python
from sys import stdin
from itertools import combinations


input = stdin.readline


a=list(map(int,input().split()))
o = []
e = []

for c in range(1,4):
    for cc in combinations(a,c):
        t = cc[0]
        for i in range(1,c):
            t*=cc[i]
        if t%2:
            o.append(t)
        else:
            e.append(t)

if len(o):
    o.sort(reverse=True)
    print(o[0])
else:
    e.sort(reverse=True)
    print(e[0])
```