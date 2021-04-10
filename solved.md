---
layout: post
title: boj 2921 해설
categories: [Baekjoon]
tags: [백준 2921, boj 2921]
---

[백준 2921번](https://www.acmicpc.net/problem/2921)
======

수학

-----
수학 문제!!

```python
n = int(input())
res = 0
for i in range(1,n+1):
    res += i*(i+1)
    res += (i+1)*i//2
print(res)
```