---
layout: post
title: boj 13305 해설
categories: [Baekjoon]
tags: [백준 13305, boj 13305]
---

[백준 13305번](https://www.acmicpc.net/problem/13305)
======

그리디

-----
그으리이디 추천문제로 풀어봤는데 쉽다. 시간 복잡도는 O(n)이다.

```python
from sys import stdin,maxsize


input = stdin.readline

n = int(input())
l = list(map(int,input().split()))
v = list(map(int,input().split()))

res = v[0]*l[0]
prev = v[0]
for i in range(1,n-1):
    if prev>v[i]:
        prev=v[i]
    res += l[i]*prev
    
print(res)
```